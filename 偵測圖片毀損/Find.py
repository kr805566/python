
import os
from CheckImage import CheckImage


class CheckBrockImage(object):
    def __init__(self, train_dir):
        self.train_dir = train_dir
        self.completeFile = 0
        self.incompleteFile = 0
    def get_imgs(self):
        """搜尋底下圖片"""
        for file in os.listdir(self.train_dir):
            if os.path.splitext(file)[1].lower() == '.jpg' or os.path.splitext(file)[1].lower() == ".jpeg":
                ret = self.check_img(file)
                if ret:
                    self.completeFile += 1

                else:
                    self.incompleteFile = self.incompleteFile + 1
                    self.img_remove(file)  # 删除不完整图片

    def img_remove(self, file):
        """刪除圖片"""
        os.remove(self.train_dir + file)

    def check_img(self, img_file):
        """檢測圖片"""
        return CheckImage(self.train_dir + img_file).check_jpg_jpeg()

    def run(self):
        """執行程式"""
        self.get_imgs()

        print('毀損圖片 : %d個' % self.incompleteFile)
        print('正常圖片 : %d個' % self.completeFile)

if __name__ == '__main__':


    #自動抓train下一層的資料夾
    #./train/景點A/Image.jpg
    #./train/景點B/Image.jpg
    #...
    #./train/景點Z/Image.jpg


    Ldir = './train/'
    for Rdir in os.listdir(Ldir):
        print('正在檢測' + Rdir + ':')
        train_dir = Ldir + Rdir + '/'   # 检测文件夹
        imgs = CheckBrockImage(train_dir)
        imgs.run()
