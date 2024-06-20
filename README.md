# EducaTour Modelv1 (Transfer Learning from Xception)
 Xception model stands for "Extreme Inception." The Inception architecture is used as a foundation, but depthwise separable convolutions are used instead of the regular Inception modules. A more effective model with enhanced performance is the end outcome of this.

### What is Depthwise Separable Convolutions?
Depthwise Separable Convolutions factorize a standard convolution into a depthwise convolution (which applies a single filter to each input channel) followed by a pointwise convolution (which applies a 1x1 convolution to combine the outputs from the depthwise convolution).
![alt text][xception-arch]
Source: [Review: Xception — With Depthwise Separable Convolution, Better Than Inception-v3 (Image Classification)](https://towardsdatascience.com/review-xception-with-depthwise-separable-convolution-better-than-inception-v3-image-dc967dd42568)

### Model Information
You can access the model [here](https://drive.google.com/drive/folders/1lFiWeZeTB6w_rf5CDLcvLtfAa96Vr1Ci?usp=drive_link)  
- **modelv1-ft-98.h5** : Fine-tuned model with 98% final accuracy
- **modelv1-preft-88.h5** : Unweighted model with 88% final accuracy

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