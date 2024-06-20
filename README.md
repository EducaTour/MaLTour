# EducaTour Model (Transfer Learning from EfficientNetV2B0, DenseNet121, Xception)
In creating machine learning models for EducaTour, we created 3 different models, all three using the transfer learning method. Where the three pre-trained model architectures are EfficientNetV2B0, Dense121, and Xception. The aim of making these three models is to compare which model is the best of the three models. The elements reviewed are model accuracy and model size. A good model is a model that has the highest accuracy and the smallest size.

## Introduction
1. EfficientNet was created by Mingxing Tan and Quoc V. Le from Google in 2019. EfficientNet uses compound coefficients to uniformly scale the depth (number of layers), breadth (number of channels), and resolution of input images on a CNN network. This is different from other architectural approaches which carry out this scaling irregularly. From the research results, EfficientNet's accuracy on ImageNet data significantly outperforms other CNN architectures. Therefore, the EfficientNet model architecture was chosen to create a model using the transfer learning methods.
2. Xception model stands for "Extreme Inception." The Inception architecture is used as a foundation, but depthwise separable convolutions are used instead of the regular Inception modules. A more effective model with enhanced performance is the end outcome of this.
3. DenseNet121 (Dense Convolutional Network) is an architecture that focuses on making the deep learning networks go even deeper, but at the same time making them more efficient to train, by using shorter connections between the layers. DenseNet is a convolutional neural network where each layer is connected to all other layers that are deeper in the network, that is, the first layer is connected to the 2nd, 3rd, 4th and so on, the second layer is connected to the 3rd, 4th, 5th and so on. This is done to enable maximum information flow between the layers of the network. To preserve the feed-forward nature, each layer obtains inputs from all the previous layers and passes on its own feature maps to all the layers that will come after it. Source: [Creating DenseNet 121 with TensorFlow](https://towardsdatascience.com/creating-densenet-121-with-tensorflow-edbc08a956d8)

## Additional Strategy
For the EfficientNet model, there was a particular strategy, Which is to train several layers in the network, namely the layers at the back and the fully connected/DNN layer. In this case, the number of back layers to be trained with the prepared training set must be determined first. In this strategy, 125 back layers in the EfficientNet architecture are retrained and the rest are retained (frozen).

For the Xception model, the strategy was use depthwise separable convolutions are used instead of the regular Inception modules. So a more effective model with enhanced performance is the end outcome of this. Depthwise Separable Convolutions factorize a standard convolution into a depthwise convolution (which applies a single filter to each input channel) followed by a pointwise convolution (which applies a 1x1 convolution to combine the outputs from the depthwise convolution). 
![alt text][xception-arch]
Source: [Review: Xception — With Depthwise Separable Convolution, Better Than Inception-v3 (Image Classification)](https://towardsdatascience.com/review-xception-with-depthwise-separable-convolution-better-than-inception-v3-image-dc967dd42568)

## Model Information
You can access all the three models [here](https://drive.google.com/drive/folders/10V5Z3o4rDMZQO_G7K_Dt6571nVGkCzN4?usp=sharing)

## Training and Validation Accuracy & Loss
![alt text][acc-n-loss]

## Confusion Matrix Comparison
### Before Fine Tuned
![alt text][cm-1]
### After Fine Tuned
![alt text][cm-2]

## Prediction Preview Comparison
### Before Fine Tuned
![alt text][pre-1]
### After Fine Tuned
![alt text][pre-2]

[xception-arch]: https://miro.medium.com/v2/resize:fit:863/1*VvBTMkVRus6bWOqrK1SlLQ.png "Xception Architecture"
[acc-n-loss]: ./assets/__results___56_0.png "Training and Validation Accuracy & Loss"
[cm-1]: ./assets/__results___46_0.png "Confusion Matrix Before Fine Tuned"
[cm-2]: ./assets/__results___65_0.png "Confusion Matrix After Fine Tuned"
[pre-1]: ./assets/__results___42_0.png "Prediction Preview Before Fine Tuned"
[pre-2]: ./assets/__results___62_0.png "Prediction Preview After Fine Tuned"
