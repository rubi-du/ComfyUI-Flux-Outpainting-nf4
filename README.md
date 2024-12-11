<h1 align="center">ComfyUI-Flux-Inpainting</h1>  

  
## Introduction  
This repository wraps the flux fill model as ComfyUI nodes. Use NF4 flux fill model, support for inpainting and outpainting image. Compared to the flux fill dev model, these nodes can use the flux fill model to perform inpainting and outpainting work under lower VRM conditions<br>  

## Installation   
  
#### Method 1:  
  
1. Navigate to the node directory, `ComfyUI/custom_nodes/`  
2. `git clone https://github.com/rubi-du/ComfyUI-Flux-Inpainting.git`  
3. `cd ComfyUI-Flux-Inpainting`  
4. `pip install -r requirements.txt`  
5. Restart ComfyUI  
  
#### Method 2:  
Directly download the node source code package, unzip it into the `custom_nodes` directory, and then restart ComfyUI.  
  
#### Method 3:  
Install via ComfyUI-Manager by searching for "ComfyUI-Flux-Inpainting".  
  
## Usage  
  
Example workflows are placed in `ComfyUI-Flux-Inpainting/workflow`.<br/>  
  
### Models
The node needs to load the transformer and text_decoder_2 submodels from the `FLUX.1-Fil-dev-nf4` model and load other submodels from `FLUX.1-Fil-dev`, so these two models need to be placed in the models folder
<br/>
Model download links:<br/>  
FLUX.1-Fil-dev: https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev<br/>  
FLUX.1-Fil-dev-nf4: https://huggingface.co/sayakpaul/FLUX.1-Fill-dev-nf4<br/> 

The directory structure is as follows:<br/>  
```
ComfyUI/models/
└── FLUX.1-Fill-dev
    ├── vae
    └── scheduler
    └── text_encoder
    └── ...
└── FLUX.1-Fill-dev-nf4
    ├── transformer
    └── text_decoder_2
```

### Workflows 
Usage of inpainting workflow<br/>  
[Workflow Address](./workflow/inpainting.json)  
![plot](./assets/inpainting.png)  
  
___  
Usage of outpainting workflow<br/>  
[Workflow Address](./workflow/outpainting.json)  
![plot](./assets/outpainting.png)  