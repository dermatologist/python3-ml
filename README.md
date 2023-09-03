# :fuelpump: [OpenFaaS](https://www.openfaas.com/) Templates for deploying machine learning models and LLM agents on the cloud.

## Templates available in this repository:

- **conda-ml** (Base container with conda. Falls back to pip if conda install fails. Use torch/tf for cpu). See example ***requirements.txt*** below.
```
torch==1.13.0+cpu
torchvision==0.14.0+cpu
```
- **conda-ml-kf** (Copy of above with KubeFlow support [Read more](https://nuchange.ca/2022/12/using-openfaas-containers-in-kubeflow.html))
- **conda-langroid** (Simple OpenFaaS wrapper for [langroid](https://github.com/langroid/langroid))
- opencv-face
- gensim-text
- ~~fastai-vision~~ Deprecated
- ~~fastai-statedict~~ Deprecated
- More to come

## Downloading the templates
```
faas-cli template pull https://github.com/dermatologist/python3-ml
```

# Using the template
Create a new function (Check the templates available above)
```
faas-cli new --lang <template-name> <fn-name>
```
Build, push, and deploy
```
faas-cli up -f <fn-name>.yml
```
Test the new function
```
echo -n content | faas-cli invoke <fn-name>
```
## Give us a star ⭐️
If you find these templates useful, give us a star. It helps others discover them.
## Contributors

* [Bell Eapen](https://nuchange.ca) |  [Contact](https://nuchange.ca/contact)
