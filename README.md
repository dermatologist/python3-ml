# python3-ml

[OpenFaaS](https://www.openfaas.com/) Template for deploying fastai and other machine learning models on the cloud.

## Templates available in this repository:

- fastai-vision
- opencv-face
- gensim-text
- fastai-statedict
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
## Contributors

* [Bell Eapen](https://nuchange.ca) |  [Contact](https://nuchange.ca/contact)
