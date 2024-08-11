# QGIS_KML_to_DJI_Pilot_2

A script that converts the KML export from QGIS into a KML file that is readable by the DJI Pilot 2 app.

## Usage

There are 2 options for running this script:

### Windows Executable

1. Clone this repository to your local machine.
2. Navigate to the `dist` directory, where you will find the standalone `.exe` executable file.
3. Double click the `.exe` file to run the script.
4. Follow the prompts to select your input KML file and export location.

### Linux Executable (for Debain based systems)

1. Clone this repository to your local machine.
2. Navigate to the `dist` directory, where you will find the standalone `.deb` Debain package file.
3. Double click the `.deb` file to install.
4. In the terminal, enter `QGIS-KML-to-DJI-Pilot-2`.
5. Follow the prompts to select your input KML file and export location.

### Python Script

1. Ensure that Python 3 is installed on your computer.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the script using a terminal or command prompt.
4. Run the script with the following command: `python main.py`
5. Follow the prompts to select your input KML file and export location.

* For best results, `cd` to cloned folder in a conda terminal and set-up with `conda env create -f environment.yml -n QGIS_KML_to_DJI_Pilot_2`

### Citation

Please cite however you can if you use this script

@misc{lehnen2023qgiskml,
  author = {Lehnen, Charles},
  title = {QGIS_KML_to_DJI_Pilot_2},
  year = {2023},
  howpublished = {\url{https://github.com/CharlesLehnen/QGIS_KML_to_DJI_Pilot_2}}
}

Original inspiration thanks to @LV_Forestry from [this post](https://forum.dji.com/thread-283890-1-1.html).

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE.md](LICENSE) file for details.
