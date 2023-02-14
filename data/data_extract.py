import os
from zipfile import ZipFile
import pandas as pd
import sys
import shutil
import glob

def copy_files_to_dest_folder(src, dest):
    # Source path
    # src = '/Users/AmirPurified/Documents/Work/data_scrap/test_2021/data'
        
    # Destination path 
    # dest = '/Users/AmirPurified/Documents/Work/data_scrap/test_2021/all_data/'

    #check if directory exists
    if os.path.exists(dest):
        print("\nfile already exists! {}".format(dest))
    
      # make the directory
    if not os.path.exists(dest):
        os.makedirs(dest, exist_ok=True)

    # # Copy the content of 
    # # source to destination 
    # destination = shutil.copytree(src, dest, dirs_exist_ok=True) 

    # src_files = os.listdir(src)
    files_list = []
    for root, subdirs, files in os.walk(src):
        # print('--\nroot = ' + root)
        # list_file_path = os.path.join(root, 'my-directory-list.txt')
        # print('list_file_path = ' + list_file_path)
        for file in files:
            if file != '.DS_Store':
                files_list.append(os.path.join(root, file))
    print (files_list)
    for file_name in files_list:
        # full_file_name = os.path.join(src, file_name)
        if os.path.isfile(file_name):
            print (file_name)
            shutil.copy(file_name, dest)

def extract_zip(folder_path):
    names = os.listdir(folder_path)
    print (names)
    for name in names:
        try:
            path = os.path.abspath(name)
            # print (folder_path+'/'+name)
            with ZipFile(folder_path+'/'+name, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
                zipObj.extractall(path=folder_path)

            print (name + ' --sucessful')
        except:
            print ("folder not existed")
            pass
    print('All done')

def merge_csv(folder_path):
    folder_path = folder_path
    print ('extracted csv folder: ',folder_path)
    names = sorted(os.listdir(folder_path))
    [print(i + ' --found') for i in names]
    ## print (names + ' --found' )
    var_dict = {}


    for i,name in enumerate(names):
        if name != '.DS_Store' and name != 'TEST.csv' and name != 'concated.csv':

            # full_path = folder_path+'/'+name
            full_path = os.path.join(folder_path, name)
            var_dict[f'df{i}'] = pd.read_csv(full_path, index_col=0, names=['Open_time',
            'Open','High','Low','Close','Volume','Close_time','Quote_asset_volume','Number_of_trades',
            'Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Ignore'])
        else:
            pass
    # print (var_dict)
    concat_df = pd.concat(var_dict.values())

    # time column is converted to "YYYY-mm-dd hh:mm:ss" ("%Y-%m-%d %H:%M:%S")
    # print (concat_df.info())
    posix_time = pd.to_datetime(concat_df.index, unit='ms')

    # append posix_time
    concat_df.insert(0, "Date", posix_time)
    
    # # drop unix time stamp
    # concat_df.drop('Open_time', axis = 1, inplace = True) 
    save_path = (folder_path+"/concated.csv")
    # print (save_path)
    concat_df.to_csv(save_path)
    print ('extracetd csv save: ', save_path)

def remove_extracted_files(dest):
    files = glob.glob(dest+"/*")
    for f in files:
        print (f)
        if f != dest+"concated.csv":
            
            os.remove(f)


def main():
    src = '/Users/AmirPurified/Documents/Work/data_scrap/test_2021/data'
    dest = '/Users/AmirPurified/Documents/Work/data_scrap/test_2021/extracted_data/'
    copy_files_to_dest_folder(src, dest)
    extract_zip(dest)
    merge_csv(dest)
    remove_extracted_files(dest)


if __name__ == '__main__':
    main()

