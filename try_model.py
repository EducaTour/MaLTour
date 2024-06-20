import tensorflow as tf
import numpy as np
import pickle

class Inference():
    def __init__(self, model_path: str, classes: list, target_size: tuple=(224,224)):
        self.model_path = model_path
        self.classes = classes
        self.target_size = target_size

        try:
            self.__loaded_model = tf.keras.models.load_model(self.model_path)
            # self.__inference_func = self.__loaded_model.signatures['serving_default']
            # with open(model_path) as f:            
            #     self.__loaded_model = pickle.load(f)
        except Exception as e:
            print("err load")

        self.__prepared_img = None

    def model_summary(self):
        try:
            return self.__loaded_model.summary()
        except Exception as e:
            return e

    def __preprocess_img(self, img):
        img = tf.io.read_file(img)
        img = tf.io.decode_image(img)
        img = tf.image.resize(img, self.target_size)
        return img

    def predict_class(self, img):
        img = self.__preprocess_img(img)
        try:
            # return self.__inference_func
            pred_prob = self.__loaded_model.predict(tf.expand_dims(img, axis=0))
            pred_cat = pred_prob.argmax(axis=-1)
            pred_class = self.classes[pred_cat[0]]

            th = 65
            final_pb = round(np.max(pred_prob)*100, 2)
            
            return ("Undefined", None) if final_pb < th else (pred_class ,final_pb) 

        except Exception as e:
            return e
        

if __name__ == "__main__":
    LABELS = sorted(['benteng_vredeburg', 'candi_borobudur', 'candi_prambanan', 'garuda_wisnu_kencana',
                     'gedung_sate', 'istana_maimun', 'jam_gadang', 'keong_mas', 'keraton_jogja', 'kota_tua',
                     'lawang_sewu', 'masjid_istiqlal', 'masjid_menara_kudus', 'masjid_raya_baiturrahman',
                     'menara_siger_lampung', 'monas', 'monumen_bandung_lautan_api', 'monumen_gong_perdamaian',
                     'monumen_nol_km', 'monumen_simpang_lima_gumul', 'patung_ikan_surabaya', 'patung_yesus_memberkati',
                     'tugu_jogja', 'tugu_khatulistiwa', 'tugu_pahlawan_surabaya'])


    #Instantiate
#    M = Inference(model_path="./history/mode",
    M = Inference(model_path="./history/best_model_2.h5",
                      target_size=(224, 224),
                    #   target_size=(300, 300),
                      classes=LABELS)

    # M.model_summary()

    # colab_path = "./data-predict-on-new-img/candi-prambanan1.jpeg"
    # colab_path = "./test-real-data/web3-washington-dc-monument-reflection-shutterstock_1140788474.jpg"
    
    import os
#    root_path = ".https://cloud.jpnn.com/photo/arsip/normal/2022/07/02/suasana-hari-pertama-prambanan-jazz-festival-2022-di-kawasan-j3kg.jpg"
#    root_path = "./data-predict-on-new-img"
#    root_path = "./test-undefined-data"
    root_undef = "./test-undefined-data"
    root_real = "./data-predict-on-new-img"
    list_undef = os.listdir("./test-undefined-data")
    test_img_undef = [os.path.join(root_undef, x) for x in list_undef]
    list_real = os.listdir("./data-predict-on-new-img")
    test_img_real = [os.path.join(root_real, x) for x in list_real]

    test_img_p = test_img_undef + test_img_real

    for i, x in enumerate(test_img_p):
        classes, prob = M.predict_class(x)
        print(f"""
path: {test_img_p[i].split("/")[-1]}
prob: {classes} | {prob}%
              \n""")
    
    print("tf version:", tf.__version__)
    
    
    
    # def change_layer_names(self, model):
    #     try:
    #         for l in model.layers:
    #             l._name = l.name.replace("_","-")  # sesuaiin aja args nya
    #     except Exception as e:
    #         print(e)

    # def show_layer_names(self):
    #     try:
    #         for i, l in enumerate(self.__loaded_model.layers):
    #             print(i, l.name)
    #     except Exception as e:
    #         print(e)
