# External Imports
import os
import filetype



def is_file_wav(path : str) -> bool :
    """
        ## is_file_wav

        ### params :
            path : path to check of the file is a wav file or not
        ### return :
            True if the file is a .wav file, False instead
    """

    if not os.path.exists(path) or not os.path.isfile(path) :
        return False
        
    kind = filetype.guess(path)
    return kind is not None and kind.extension == "wav"
# def is_file_wav(path : str) -> bool 




def edit_opensmile_configuration(feature_extractor : str, frame_size : float, frame_step : float) :
    def replace_line(file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()
    # def replace_line(file_name, line_num, text)


    if feature_extractor == "COMPARE" :
        replace_line("./Ressources/opensmile/config/compare/ComParE_2016_core.lld.conf.inc", 18 - 1, f"frameSize = {frame_size} \n")
        replace_line("./Ressources/opensmile/config/compare/ComParE_2016_core.lld.conf.inc", 19 - 1, f"frameStep = {frame_step} \n")
        replace_line("./Ressources/opensmile/config/compare/ComParE_2016_core.lld.conf.inc", 51 - 1, f"frameSize = {frame_size} \n")
        replace_line("./Ressources/opensmile/config/compare/ComParE_2016_core.lld.conf.inc", 52 - 1, f"frameStep = {frame_step} \n")
    elif feature_extractor in ["EGEMAPS", "GEMAPS"] :
        replace_line("./Ressources/opensmile/config/gemaps/v01b/GeMAPSv01b_core.lld.conf.inc", 20 - 1, f"frameSize = {frame_size} \n")
        replace_line("./Ressources/opensmile/config/gemaps/v01b/GeMAPSv01b_core.lld.conf.inc", 21 - 1, f"frameStep = {frame_step} \n")
        replace_line("./Ressources/opensmile/config/gemaps/v01b/GeMAPSv01b_core.lld.conf.inc", 53 - 1, f"frameSize = {frame_size} \n")
        replace_line("./Ressources/opensmile/config/gemaps/v01b/GeMAPSv01b_core.lld.conf.inc", 54 - 1, f"frameStep = {frame_step} \n")