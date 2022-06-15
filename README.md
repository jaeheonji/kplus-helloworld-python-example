# kplus-helloworld-python-example

This repository shows how to construct an [istio-helloworld](https://github.com/istio/istio/tree/master/samples/helloworld) using `cdk8s+`

# Getting Started

1. **Clone this repo and install requirements**

```bash
git clone https://github.com/jaeheonji/kplus-helloworld-python-example.git
cd kplus-helloworld-python-example

# (optional) setting up virtualenv 
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

2. **Generate kubernetes manifest**

```bash
python main.py
```

Then `helloworld.k8s.yaml` will be created in `dist` folder.

3. **(optional) Generate low-level constructs for istio CRD(Custom Resource Deifinition)**

To define an istio CRD in `cdk8s+`, you must first create an `imports` files. Although this repository already contains the generated `imports`, the following requirements are required to create a new one.

* [cdk8s-cli](https://cdk8s.io/docs/latest/cli/installation/)
* istio CRD ([crd-all.gen.yaml](https://github.com/istio/istio/blob/master/manifests/charts/base/crds/crd-all.gen.yaml))

Then execute the command as follows:

```bash
cdk8s import -l python crd-all.gen.yaml
```
