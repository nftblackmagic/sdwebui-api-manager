from pydantic import BaseModel
from typing import List


class Answer(BaseModel):
    question_id: int
    alternative_id: int


class UserAnswer(BaseModel):
    user_id: int
    answers: List[Answer]

class Img2imgArgs(BaseModel):
  init_images: List[str]
  resize_mode: int
  denoising_strength: float
  image_cfg_scale: int
  mask: str
  mask_blur: int
  inpainting_fill: int
  inpaint_full_res: bool
  inpaint_full_res_padding: int
  inpainting_mask_invert: bool
  initial_noise_multiplier: int
  prompt: str
  styles: List[str]
  seed: int
  subseed: int
  subseed_strength: int
  seed_resize_from_h: int
  seed_resize_from_w: int
  sampler_name: str
  batch_size: int
  n_iter: int
  steps: int
  cfg_scale: int
  width: int
  height: int
  restore_faces: bool
  tiling: bool
  do_not_save_samples: bool
  do_not_save_grid: bool
  negative_prompt: str
  eta: int
  s_min_uncond: int
  s_churn: int
  s_tmax: int
  s_tmin: int
  s_noise: int
  override_settings: dict
  override_settings_restore_afterwards: bool
  script_args: List[dict]
  sampler_index: str
  include_init_images: bool
  script_name: str
  send_images: bool
  save_images: bool
  alwayson_scripts: dict