# External Imports
import audiofile
import opensmile
import argparse
import os
import pandas as pd



# Internal Imports
from src.utils import is_file_wav, edit_opensmile_configuration


OPENSMILE_FEATURES_EXTRACTORS_PATH : dict = {
    "COMPARE" : './Ressources/opensmile/config/compare/ComParE_2016.conf',
    "GEMAPS" : './Ressources/opensmile/config/gemaps/v01b/GeMAPSv01b.conf',
    "EGEMAPS" : './Ressources/opensmile/config/egemaps/v02/eGeMAPSv02.conf'
}



if __name__ == "__main__" : 
    arg_parser = argparse.ArgumentParser(description='A test program.')
    arg_parser.add_argument('--indir', help='Input file directory', type=str)
    arg_parser.add_argument('--feature_extractor', help="OpenSmile feature extractor (COMPARE ; GEMAPS ; EGEMAPS)", type=str)
    arg_parser.add_argument('--frame_size', help='frame size in seconds', type=float, default=0.2)
    arg_parser.add_argument('--frame_step', help='frame size in seconds', type=float, default=0.2)
    args = arg_parser.parse_args()

    assert os.path.isdir(args.indir)


    feature_extractor_path : str = OPENSMILE_FEATURES_EXTRACTORS_PATH.get(args.feature_extractor, None)
    assert feature_extractor_path is not None
    
    indir : str = args.indir
    inputs_files = os.listdir(indir)
    for file in inputs_files :
        file_path = os.path.join(indir, file)


        if not is_file_wav(file_path) :
            continue
            
        print("Processing file ", file_path)
        
        edit_opensmile_configuration(args.feature_extractor, args.frame_size, args.frame_step)

        smile = opensmile.Smile(
            feature_set=feature_extractor_path,
            feature_level='lld',
        )

        signal, sampling_rate = audiofile.read(
            file_path
        )

        result_df : pd.DataFrame = smile.process_signal(
            signal,
            sampling_rate
        )

        common_outpath : str = os.path.splitext(file_path)[0] 
        outpath : str = f"{common_outpath}_{args.feature_extractor}.csv"
        result_df.to_csv(outpath)