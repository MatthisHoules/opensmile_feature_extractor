# Open Smile feature Extractor


This repository allows to use the OpenSmile feature extractor with a custom frame size and frame step.

## License
As OpenSmile and OpenSmile-Python are licensed softwares, use of this directory must therefore comply with the opensmile licence.


### OpenSmile License :
openSMILE follows a dual-licensing model. Since the main goal of the project is a widespread use of the software to facilitate research in the field of machine learning from audio-visual signals, the source code and binaries are freely available for private, research, and educational use under an open-source license (see LICENSE). It is not allowed to use the open-source version of openSMILE for any sort of commercial product. Fundamental research in companies, for example, is permitted, but if a product is the result of the research, we require you to buy a commercial development license. Contact us at info@audeering.com (or visit us at https://www.audeering.com) for more information.


## Installation 

```
git clone https://github.com/MatthisHoules/opensmile_feature_extractor.git
cd ./opensmile/feature_extractor
pip install -r requirements.txt
```

## Usage 
```
python ./main.py --indir <Input_files_repository> --feature_extractor <feature_extractor_name> --frame_size <frame_size_float_in_seconds> --frame_step <frame_step_float_in_seconds>
```

Please note :
- feature_extractor possibilities are ["COMPARE", "EGEMAPS", "GEMAPS"]
- frame_size and frame_step arguments are not mandatories : default is 200ms.

