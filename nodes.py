
import os

import numpy as np
import torch
from .modules.load_util import load_flux_fill_nf4
from folder_paths import models_dir


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

_pipeline = None

class FluxNF4Inpainting:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            
        }
        
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "inpainting"
    CATEGORY = "Inpainting"
        
    def outpainting(self,
                    prompt,
                    image,
                    mask_image,
                    num_inference_steps,
                    cached,
                    ):
        
        global _pipeline
        
        pipeline = _pipeline
        if not cached or pipeline is None:
            flux_dir = os.path.join(models_dir, "FLUX.1-Fill-dev")
            if not os.path.isdir(flux_dir):
                flux_dir = "black-forest-labs/FLUX.1-Fill-dev"
            
            flux_nf4_dir = os.path.join(models_dir, "FLUX.1-Fill-dev-nf4")
            if not os.path.isdir(flux_nf4_dir):
                flux_nf4_dir = "sayakpaul/FLUX.1-Fill-dev-nf4"
            _pipeline = load_flux_fill_nf4(
                flux_dir=flux_dir,
                flux_nf4_dir=flux_nf4_dir,
                four_bit=True
            )
            _pipeline.enable_model_cpu_offload()
            pipeline = _pipeline
            
            res = pipeline(
                prompt=prompt,
                image=image,
                mask_image=mask_image,
                num_inference_steps=num_inference_steps,
            )
            
            return pil2tensor(res.images[0])
            
            

NODE_CLASS_MAPPINGS = {
    "Flux Inpainting": FluxNF4Inpainting
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Flux Inpainting": "Flux Inpainting"
}

            
        
        
        