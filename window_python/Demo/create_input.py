from files import ReFilenames, SaveFile

class Gaussian_input():
    def __init__(self):
        pass

    def main(self, filename):
        all_names_obj = ReFilenames("gjf")
        write_file = SaveFile()
        all_names_list = all_names_obj.get_all_files(filename, True, True)
        all_file_list = all_names_obj.get_all_files(filename)
        for name, file_name in zip(all_names_list,all_file_list):
            # 应该增加存在文件应该先删除，以免重复写入，造成文件有问题
            new_name = name + "_new.gjf"
            replace_name = name + "_new"
            cont_list = list(self.contents(replace_name).split("\n"))
            write_file.save_n(new_name, cont_list[1:11])
            write_file.save(new_name, self.read_coordinates(file_name))
            write_file.save_n(new_name, cont_list[11:])

    def read_coordinates(self, filename):
        coordinate_list = []
        write_flag = False
        with open(filename) as file_obj:
            for line in file_obj.readlines():
                if write_flag:
                    coordinate_list.append(line)
                if "0 1" in line:
                    write_flag = True
        return coordinate_list
                

    def contents(self, name):
        return_contents = """
%chk=C4-im1.chk
%mem=100GB
%nprocshared=64
%rwf=/home3/scratch_x/C4-im1.rwf
#p oniom(ROCCSD(T,T1diag,maxcyc=200,Conver=6)/6-31+G(d'):m062x/6-31++g(d,p)) 
scrf=solvent=n,n-dimethylformamide

Title Card Required

0 1


--Link1--
%chk=C4-im1.chk
%mem=100GB
%nprocshared=64
%rwf=/home3/scratch_x/C4-im1.rwf
# MP4SDQ/CBSB4 Geom=AllCheck Guess=Read SCRF=Check


        """
        return return_contents.replace("C4-im1", name)

if __name__ == '__main__':
    A = Gaussian_input()
    #B = A.main(r"E:\Orginzed Files\2022.10.10.14.18-备份文件\文章全数据\gas")
    C = A.main(r"C:\Users\熊孩子\Desktop\DL-CBS (2)\new_test")
    print (C)

    #write_file = SaveFile()
    #B = A.contents("A")
    #C = list(B.split("\n"))
    #print(C)
    #write_file.save("test.txt", C)
