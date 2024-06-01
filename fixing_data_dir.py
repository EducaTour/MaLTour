import os
import numpy as np
import shutil
# import re

def move_data_to_tmp(source_path, target_path, labels:list):
    
    try:                    
        for sd in labels:
            os.makedirs(os.path.join(target_path, sd))
    except FileExistsError: 
        print(os.listdir(target_path))
    except Exception as e: print(e)
    
    source_data = os.listdir(source_path)
    tmp_img = []
    total_fixed_img = 0
    
    for d in source_data:
        dir_path = os.path.join(source_path, d)
        for i, subdir in enumerate(os.listdir(dir_path)):        
            subdir_path = os.path.join(dir_path, subdir)            
            # i+=1
            for img in os.listdir(subdir_path): 
                img_path = os.path.join(subdir_path, img)
                tmp_img.append(img_path)
                
                # print(LABELS[i])
                # print(i)
                dst_img_path = os.path.join(target_path, labels[i], f"{img}")
                # # print(dst_img_path)
                # print(img_path)     
                
                try:
                    if ".jpg" in img_path.lower() or ".png" in img_path.lower():            
                        # print(img_path)  
                        if os.path.exists(dst_img_path):
                            print("Duplicate!!!")
                            print(f"Before: {dst_img_path} | ",end=None)
                            dst_img_path_r = os.path.join(target_path, labels[i], f"{str(i)}_{labels[i]}_{img}")
                            print("After:",dst_img_path_r)
                            shutil.copy(img_path, dst_img_path)                             
                            total_fixed_img += 1
                        else:
                            shutil.copy(img_path, dst_img_path) 
                            total_fixed_img += 1
                    else:
                        print(img_path)
                except Exception as e:
                    print(e)

    print("total img:", total_fixed_img)


# def create_train_val_dirs(root_path, labels:list):
#     try:
#         if os.path.exists(root_path):
#             shutil.rmtree(root_path)
#         else:
#             os.makedirs(root_path)
        
#         for d in ["train", "val"]:
#             for i, sd in enumerate(labels):
#                 n = os.path.join(root_path, d, sd)
#                 os.makedirs(n)
#                 print(n)
        
#     except Exception as e:
#         print(e)



if __name__ == "__main__":
    
    LABELS = sorted(
        [
            "monas", "kota_tua", "gedung_sate", "candi_borobudur", "candi_prambanan", "lawang_sewu", "keraton_jogja",
            "monumen_bandung_lautan_api", "benteng_vredeburg", "jam_gadang", "patung_ikan_surabaya", "tugu_jogja",
            "garuda_wisnu_kencana", "masjid_raya_baiturrahman", "masjid_istiqlal", "monumen_nol_km", "tugu_khatulistiwa",
            "monumen_simpang_lima_gumul", "menara_siger_lampung", "istana_maimun", "patung_yesus_memberkati", "tugu_pahlawan_surabaya",
            "keong_mas", "monumen_gong_perdamaian", "masjid_menara_kudus"
        ]
    )
    
    fixed_dir_path = "./fixed_data_dir"
    raw_dir_path = "./raw_data_dir"
    tmp_dir_path = "./data-test"
    
    move_data_to_tmp(raw_dir_path, tmp_dir_path, labels=LABELS)
    # create_train_val_dirs(fixed_dir_path, labels=LABELS)