# Transfer Learning for Sound-Based Fault Detection in Industrial Machinery

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

This Jupyter Notebook project focuses on utilizing transfer learning techniques to enhance sound-based fault detection in industrial machinery. By leveraging the pre-trained VGG16 architecture and the Keras deep learning framework, we aim to transfer knowledge from sound event detection tasks to the domain of fault detection, achieving superior performance and accuracy.

## Project Highlights

- Application of transfer learning techniques to sound-based fault detection.
- Utilization of the VGG16 pre-trained model for feature extraction.
- Seamless development and training of deep learning models using the Keras framework.
- Evaluation of the model's performance in detecting faults in industrial machinery.
- Comparison with traditional methods for fault detection.

## Dataset

We used the "MIMII DATASET: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection" for training and testing our models. This dataset contains a wide variety of industrial machine sounds that encompass different fault types. You can download the dataset from [here](https://zenodo.org/record/3384388).

## Installation and Setup

To replicate the experiments and explore the project, follow these steps:

1. Clone this repository: `git clone https://github.com/Alireza499/sound-based_fault_detection.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Download the pre-trained VGG16 weights and save them in the designated directory.
4. Customize the data loading and preprocessing scripts to fit your dataset.
5. Open the Jupyter Notebook: `jupyter notebook`
6. Run and experiment with the notebook files.

## Results and Discussion

Through this project, our objective is to achieve improved accuracy in fault detection by harnessing the power of transfer learning. The pretrained VGG16 model's ability to capture intricate sound patterns contributes to the enhanced performance in identifying faults in industrial machinery.

## License

This project is licensed under the MIT license. For more information, please refer to the license file.

## Acknowledgments

We extend our gratitude to the creators of the VGG16 architecture and the Keras deep learning framework for providing essential tools for this project. Additionally, we would like to acknowledge the authors of the "MIMII DATASET" for making their valuable dataset available for research.

For detailed insights and implementation specifics, please refer to the Jupyter Notebook files and available documentation in this repository.

---

Feel free to explore the notebooks, contribute to the project, or adapt the techniques for your own sound-based fault detection scenarios!
