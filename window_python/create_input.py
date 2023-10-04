from files import ReFilenames, SaveFile

class Gaussian_input():
    def __init__(self):
        pass

    def main(self, filename):
        all_names_obj = ReFilenames("gjf")
        write_file = SaveFile()
        all_names_list = all_names_obj.get_all_files(filename, True, True)
        for name in all_names_list:
            cont_list = list(self.contents(name).split("\n"))
            write_file.save(name + "_cbs.gjf", cont_list)

    def contents(self, name):
        return_contents = """
%chk=C4-im1.chk
%nprocshared=16
%mem=128MW
# CCSD(T,T1diag,maxcyc=200)/6-31+G(d') Geom=AllCheck Guess=Read 

Title Card Required

0 1


--Link1--
%chk=C4-im1.chk
%nprocshared=16
# MP4SDQ/CBSB4 Geom=AllCheck Guess=Read SCRF=Check



--Link1--
%chk=C4-im1.chk
%nprocshared=16
# Geom=AllCheck Guess=Read MP2/CBSB3 CBSExtrap=(NMin=10,MinPop) SCRF=Check
        """
        return return_contents.replace("C4-im1", name)

if __name__ == '__main__':
    A = Gaussian_input()
    B = A.main(r"E:\Orginzed Files\2022.10.10.14.18-备份文件\文章全数据\gas")
   

    #write_file = SaveFile()
    #B = A.contents("A")
    #C = list(B.split("\n"))
    #print(C)
    #write_file.save("test.txt", C)
