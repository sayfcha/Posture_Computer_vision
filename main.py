import cv2 
import mediapipe as mp 

cap=cv2.VideoCapture(0) #pour avoir accès à la camera 


# résolution de la video
cap.set(3,1280)  #largeur
cap.set(4,720)   #hauteur 


class PoseDetector():
    def __init__(self,static_image_mode=False,  #definit si image d'entrée est image statique ou video(flux)
               model_complexity=1,        #complexité etablis le compromis entre vitrsse et précision 
               smooth_landmarks=True,   #filtrage des landmarks 
               enable_segmentation=False,
               smooth_segmentation=True,
               min_detection_confidence=0.7,
               min_tracking_confidence=0.6):
               
        self.static_mode=static_image_mode
        self.m_complexity=model_complexity
        self.m_d_conf=min_detection_confidence
        self.m_t_conf=min_tracking_confidence

        self.mp_draw_utils=mp.solutions.drawing_utils   # utile pour afficher les landmarks 
        self.mp_pose=mp.solutions.pose 
        self.pose=mp.solutions.pose.Pose(static_image_mode=self.static_mode,
                                        model_complexity=self.m_complexity,
                                        smooth_landmarks=True,
                                        enable_segmentation=False,
                                        smooth_segmentation=True,
                                        min_detection_confidence=self.m_d_conf,
                                        min_tracking_confidence=self.m_t_conf)


    def find_pose(self,img,draw=True): 

        """fonction  qui detecte la pose dans la video"""
                                    
        rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        process=self.pose.process(rgb_img)
        plm_list=[]         #poselandmarks
        h,w,c=img.shape
        if process.pose_landmarks:
            
            


            for lm in process.pose_landmarks.landmark:
                x,y,z = int(lm.x * w),int(lm.y*h), int(lm.z * w)     # on prend la position de landmark en pixel   (lm.x pourcentage of the width)
                
                plm_list.append([x,y,z])
            #pose['plm_list']=plm_list

            if draw: 
                            self.mp_draw_utils.draw_landmarks(img,process.pose_landmarks,self.mp_pose.POSE_CONNECTIONS)



        return img, plm_list
detector= PoseDetector()
                

                    
        




#boucle pour visualiser la video et avoir les données frame par frame 

while True: 
    _,img=cap.read()
    img,landmark_list=detector.find_pose(img,False)
    
    cv2.imshow("cam",img)

    #option pour quitter  

    key=cv2.waitKey(1)

    if key ==ord("q"):   # on appuie sur q pour quitter 
        break 

cap.release()
cv2.destroyAllWindows()