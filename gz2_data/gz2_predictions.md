# gz2_predictions catalog

| colID |  column  |  type  | description |
|---| -------- | ------ | ----------- |
| 1 | GalaxyID |   int  | Unique galaxy ID of [kaggle GZ2 images](https://www.kaggle.com/jaimetrickz/galaxy-zoo-2-images)| 
| 2 | **class**|  short | 0 round elliptical • 1 in-between elliptical • 2 cigar-shaped elliptical • 3 edge-on spiral • 4 barred spiral • 5 unbarred sprial • 6 irregular • 7 merger |
| 3 | pred_vit |  short | predicted class label from Linformer network |
| 4 | pred_res |  short | predicted class label from ResNet50 |
| 5 | vitTresT |  short | 1 if ``pred_vit == class and pred_res == class`` else 0 |
| 6 | vitTresF |  short | 1 if ``pred_vit == class and pred_res != class`` else 0 |
| 7 | vitFresT |  short | 1 if ``pred_vit != class and pred_res == class`` else 0 |
| 8 | vitFresF |  short | 1 if ``pred_vit != class and pred_res != class`` else 0 |
| 9 | dr7objid |  long  | SDSS DR7 object ID |
| 10| dered_u  | double | u band magnitude, corrected for extinction: modelMag-extinction |
| 11| dered_g  | double | g    --  |
| 12| **dered_r** | double | **r band magnitude**, corrected for extinction: modelMag-extinction |
| 13| dered_i  | double | i   -- |
| 14| dered_z  | double | z   -- |
| 15| modelMag_u | double | u band magnitude, better of DeV/Exp magnitude fit |
| 16| modelMag_g | double | g -- |
| 17| modelMag_r | double | r -- |
| 18| modelMag_i | double | i -- |
| 19| modelMag_z | double | z -- |
| 20| lnLDeV_r   | double | DeVaucouleurs fit ln(likelihood) in r-band |
| 21| lnLExp_r   | double | Exponential disk fit ln(likelihood) in r-band |
| 22| petroR50_r | double | Radius containing 50% of Petrosian flux in r-band |
| 23| **petroR90_r** | double | **galaxy size** - Radius containing 90% of Petrosian flux in r-band |
| 24| **dered_g_r** | double | **color** : ``dered_g-dered_r`` |
| 25| model_g_r | double | color : ``modelMag_g-modelMag_r`` | 
| 26| **viewed_edge_on** | double |  GZ2 Task02 -- fraction of votes for edge-on • No : 0 <---> 1 : Yes |
| 27| **anything_odd**   | double |  GZ2 Task06 -- fraction of votes for anything odd? • No : 0 <---> 1 : Yes |

------

## Reference Links

- [SDSS DR7 schema browser](http://cas.sdss.org/dr7/en/help/browser/browser.asp?n=ProperMotions&t=U)
