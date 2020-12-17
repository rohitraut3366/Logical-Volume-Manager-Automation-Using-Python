import os


def authTypePass(username, password, ip):
    while True:
        os.system('tput setaf 4')
        print("""
                -------------------LVM MENU------------------------
                -        Enter 1 : Display all Disks              -
                ---------------------------------------------------
                -        Enter 2 : Display Mount Points           -
                ---------------------------------------------------
                -        Enter 3 : Create PV/VG/LV                -
                ---------------------------------------------------
                -        Enter 4 : Display PV/VG/LV               -
                ---------------------------------------------------
                -        Enter 5 : Delete PV/VG/LV                -
                ---------------------------------------------------
                -        Enter 6 : Mount LV                       -
                ---------------------------------------------------
                -        Enter 7 : UnMount                        -
                ---------------------------------------------------
                -        Enter 8 : Extend VG/LV                   -
                ---------------------------------------------------
                -        Enter 9 : Reduce VG/LV                      -
                ---------------------------------------------------
                -        Enter 10 : Exit                           -
                ---------------------------------------------------
            """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == '1':
            os.system("sshpass -p {} ssh {}@{} sudo fdisk -l".format(password, username, ip))
        elif choice == '2':
            os.system("sshpass -p {} ssh {}@{} sudo df -hT".format(password, username, ip))
        elif choice == '3':
            create = input("Enter PV/VG/LV: ")
            if create == 'PV':
                HD_name = input("Disk Name: ")
                os.system("sshpass -p {} ssh {}@{} sudo pvcreate {}".format(password, username, ip, HD_name))
            elif create == 'VG':
                HD_name = input("Enter space separated disk names: ")
                vg_name = input("Enter volume group Name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgcreate {} {}".format(password, username, ip, vg_name, HD_name))
            elif create == 'LV':
                vg_name = input("Enter volume group name: ")
                lv_name = input("Enter logical volume name: ")
                lv_size = input("Enter LV size: ")
                os.system("sshpass -p {} ssh {}@{} sudo lvcreate --name {} --size +{}G {} ".format(password, username, ip, lv_name, lv_size, vg_name))
            else:
                print("Wrong create opertion")
        elif choice == '4':
            display = input("Display PV/VG/LV : ")
            if display  == 'PV':
                os.system("sshpass -p {} ssh {}@{} sudo pvdisplay".format(password, username, ip))
            elif display == 'VG':
                os.system("sshpass -p {} ssh {}@{} sudo vgdisplay".format(password, username, ip))
            elif display == 'LV':
                os.system("sshpass -p {} ssh {}@{} sudo lvdisplay".format(password, username, ip))
            else:
                print("Wrong create opertion")
        elif choice == '5':
            delete = input("Delete PV/VG/LV : ")
            if delete == 'PV':
                delete_hd = input("Enter PV name: ")
                os.system("sshpass -p {} ssh {}@{} sudo pvremove {}".format(password, username, ip, delete_hd))
            elif delete == 'VG':
                delete_hd = input("Enter VG name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgremove {}".format(password, username, ip, delete_hd))
            elif delete == 'LV':
                vg_name = input("Enter VG name: ")
                lv_name = input("Enter LG name: ")
                os.system("sshpass -p {} ssh {}@{} sudo lvremove /dev/{}/{}".format(password, username, ip, vg_name, lv_name))
            else:
                print("Wrong create opertion")
        elif choice == '6':
            lv_name = input("ENTER NAME OF LV:")
            vg_name = input("ENTER VG NAME: ")
            os.system("sshpass -p {} ssh {}@{} sudo mkfs.ext4 /dev/{}/{}".format(password, username, ip, vg_name,
                                                                                 lv_name))
            folder = input("ENTER FOLDER NAME TO MOUNT:")
            os.system("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, ip, folder))
            os.system(
                "sshpass -p {} ssh {}@{} sudo mount /dev/{}/{} {}".format(password, username, ip, vg_name, lv_name,
                                                                           folder))
        elif choice == '7':
            folder = input("Enter folder Name")
            os.system("sshpass -p {}  ssh {}@{} sudo umount {}".format(password, username, ip, folder))

        elif choice == '8':
            extend = input("Extend VG/LV : ")
            if extend == 'LV':
                    size_change = input("ENTER SIZE TO BE INCREASED:")
                    vg_name = input("ENTER VG NAME: ")
                    lv_name = input("ENTER NAME OF LV:")
                    os.system(
                        "sshpass -p {} ssh {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(password, username, ip, size_change, vg_name, lv_name))
                    os.system(
                        "sshpass -p {} ssh {}@{} sudo resize2fs /dev/{}/{}".format(password, username, ip, vg_name,
                                                                                   lv_name))
            elif extend == "VG":
                    pv = input("Enter new PV name: ")
                    vg = input("Enter VG-Name: ")
                    os.system("sshpass -p {} ssh {}@{} sudo vgextend {} {}".format(password, username, ip, vg, pv))
            else:
                print("Wrong create opertion")
        elif choice == '9':
            reduce = input("reduce VG/LV: ")
            if reduce == 'LV':
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                new_size = input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
                if 'n' == input("lv is mounted y/n: "):
                    os.system("sshpass -p {} ssh {}@{} sudo e2fsck -f /dev/{}/{}".format(password, username, ip, vg_name, lv_name))
                    os.system("sshpass -p {} ssh {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(password, username, ip, new_size, vg_name, lv_name))
                else:
                    print("please umount lv else you might loose online work")
            elif reduce == 'VG':
                pv_name = input("PV name:  it will be remove: ")
                vg_name = input("Enter VG name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgreduce {} {}".format(password, username, ip, vg_name, pv_name))
            else:
                print("Wrong choice enter VG/LV")
        elif choice == '10':
            exit()
        else:
            print("Wrong Choice")
        input("Enter to continue")
        os.system("clear")


def authTypeKey(username, keyPath, ip):
    while True:
        os.system('tput setaf 4')
        print("""
                    -------------------LVM MENU------------------------
                    -        Enter 1 : Display all Disks              -
                    ---------------------------------------------------
                    -        Enter 2 : Display Mount Points           -
                    ---------------------------------------------------
                    -        Enter 3 : Create PV/VG/LV                -
                    ---------------------------------------------------
                    -        Enter 4 : Display PV/VG/LV               -
                    ---------------------------------------------------
                    -        Enter 5 : Delete PV/VG/LV                -
                    ---------------------------------------------------
                    -        Enter 6 : Mount LV                       -
                    ---------------------------------------------------
                    -        Enter 7 : UnMount                        -
                    ---------------------------------------------------
                    -        Enter 8 : Extend VG/LV                   -
                    ---------------------------------------------------
                    -        Enter 9 : Reduce VG/LV                      -
                    ---------------------------------------------------
                    -        Enter 10 : Exit                           -
                    ----------------------------------------------------
                    """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == '1':
            os.system("ssh -i {}  {}@{} sudo fdisk -l".format(keyPath, username, ip))
        elif choice == '2':
            os.system("ssh -i {} {}@{} sudo df -hT".format(keyPath, username, ip))
        elif choice == '3':
            create = input("Enter PV/VG/LV: ")
            if create == 'PV':
                HD_name = input("Disk Name: ")
                os.system("ssh -i {} {}@{} sudo pvcreate {}".format(keyPath, username, ip, HD_name))
            elif create == 'VG':
                HD_name = input("Enter space separated disk names: ")
                vg_name = input("Enter volume group Name: ")
                os.system(
                    "ssh -i {} {}@{} sudo vgcreate {} {}".format(keyPath, username, ip, vg_name, HD_name))
            elif create == 'LV':
                vg_name = input("Enter volume group name: ")
                lv_name = input("Enter logical volume name: ")
                lv_size = input("Enter LV size: ")
                os.system(
                    "ssh -i {} {}@{} sudo lvcreate --name {} --size +{}G {} ".format(keyPath, username, ip,
                                                                                             lv_name, lv_size, vg_name))
            else:
                print("Wrong create opertion")
        elif choice == '4':
            display = input("Display PV/VG/LV : ")
            if display == 'PV':
                os.system("ssh -i {} {}@{} sudo pvdisplay".format(keyPath, username, ip))
            elif display == 'VG':
                os.system("ssh -i {} {}@{} sudo vgdisplay".format(keyPath, username, ip))
            elif display == 'LV':
                os.system("ssh -i {} {}@{} sudo lvdisplay".format(keyPath, username, ip))
            else:
                print("Wrong create opertion")
        elif choice == '5':
            delete = input("Delete PV/VG/LV : ")
            if delete == 'PV':
                delete_hd = input("Enter PV name: ")
                os.system("ssh -i {} {}@{} sudo pvremove {}".format(keyPath, username, ip, delete_hd))
            elif delete == 'VG':
                delete_hd = input("Enter VG name: ")
                os.system("ssh -i {} {}@{} sudo vgremove {}".format(keyPath, username, ip, delete_hd))
            elif delete == 'LV':
                vg_name = input("Enter VG name: ")
                lv_name = input("Enter LG name: ")
                os.system(
                    "ssh -i {} {}@{} sudo lvremove /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            else:
                print("Wrong create opertion")
        elif choice == '6':
            folder = input("Enter folder Name")
            os.system("ssh -i {} {}@{} sudo umount -f {}".format(keyPath, username, ip, folder))
        elif choice == '7':
            lv_name = input("ENTER NAME OF LV:")
            vg_name = input("ENTER VG NAME: ")
            os.system("ssh -i  {} {}@{} sudo mkfs.ext4 /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            folder = input("ENTER FOLDER NAME TO MOUNT:")
            os.system("ssh -i {} {}@{} sudo mkdir {}".format(keyPath, username, ip, folder))
            os.system("ssh -i {} {}@{} sudo mount /dev/{}/{} {}".format(keyPath, username, ip, vg_name, lv_name, folder))
        elif choice == '8':
            extend = input("Extend VG/LV : ")
            if extend == 'LV':
                size_change = input("ENTER SIZE TO BE INCREASED:")
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                os.system("ssh -i {} {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(keyPath, username, ip, size_change, vg_name, lv_name))
                os.system(
                    "ssh -i {} {}@{} sudo resize2fs /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
            elif extend == "VG":
                pv = input("Enter new PV name: ")
                vg = input("Enter VG-Name: ")
                os.system("ssh -i {} {}@{} sudo vgextend {} {}".format(keyPath, username, ip, vg, pv))
            else:
                print("Wrong create opertion")
        elif choice == '9':
            reduce = input("reduce LV/VG: ")
            if reduce == 'LV':
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                new_size = input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
                if 'n' == input("lv is mounted y/n: "):
                    os.system("ssh -i{} {}@{} sudo e2fsck -f /dev/{}/{}".format(keyPath, username, ip, vg_name, lv_name))
                    os.system("ssh -i{} {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(keyPath, username, ip, new_size, vg_name, lv_name))
                else:
                    print("please umount lv else you might loose online work")
            elif reduce == 'VG':
                vg_name = input("Enter VG name: ")
                pv_name = input("pv name: ")
                os.system("ssh -i {} {}@{} sudo vgreduce {} {}".foramt(keypath, username, ip, vg_name, pv_name))
            else:
                print("Enter LV/VG")
        elif choice == '10':
            exit()
        else:
            print("Wrong Choice")
        input("Enter to continue")
        os.system("clear")
