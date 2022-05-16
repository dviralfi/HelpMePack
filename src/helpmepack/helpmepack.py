import os, shutil
from pathlib import Path

MODULE_DIRECTORY = Path(__file__).parent

"""
Python Package helper CLI 
"""

"""
Issues :

    * license types finder is quiet bad - need to upgrade the finding algorythm

"""


def add_LICENSE_file(LICENSE_type):
    """
    Adds the LICENSE file to root directory
    """

    if not os.path.exists('LICENSE'):
        for temp_license_type in os.listdir(os.path.join(MODULE_DIRECTORY,'all_templates\licenses_templates')):
            if LICENSE_type.lower().startswith(temp_license_type.lower()):

                # copy the template to the project directory
                template_license_file_path = "all_templates\\licenses_templates\\" + temp_license_type
                shutil.copyfile(os.path.join(MODULE_DIRECTORY,template_license_file_path), 'LICENSE')
                return

        print("LICENSE type not valid! creating Default one... (MIT) ")
        template_license_file_path = "all_templates\\licenses_templates\\" + 'mit.txt'
        shutil.copyfile(os.path.join(MODULE_DIRECTORY,template_license_file_path), 'LICENSE')
    else:
        print("LICENSE file already exists...")
        

def add_pyproject_file():
    """
    Adds the pyproject.toml file to root directory
    """

    if not os.path.exists('pyproject.toml'):
    
        shutil.copyfile(os.path.join(MODULE_DIRECTORY,'all_templates\\pyproject.toml'),'pyproject.toml')
    else:
        print("pyproject.toml file already exist...")


def add_README_file(package_name,author_name,description,url,install_requires):
    """
    Adds the README.md file to root directory
    """

    #check if the directory have a README file, and if not - make one
    if os.path.exists('README.md'):
            return

    with open('README.md','w+') as f:
        
        # writes the info that we got from the user in README.md file: 
        f.write("# "+package_name+'\n')
        f.write(description+'\n\n')
        f.write("## Developed by "+author_name+'\n')
        f.write("[Visit Package]("+url+')'+'\n\n')
        f.write("### Prerequisits\nThe dependencies of the package:"+'\n')
        for dependency in install_requires:
            f.write(dependency+'\n')
        

def add_setup_cfg_file(package_name,package_version,author_name,author_email,description,url,python_version,LICENSE_type,python_requires,install_requires):
    """
    Adds the setup.cfg file to root directory
    """

    # cehcks if the user input some dependencies of his package:
    if install_requires:
        # if yes - putting it inside setup.cfg file for the 'build' program to understand.

        install_requires_text = "install_requires = \n"+'\n'.join(install_requires)
    else:
        # no dependencies to the package - leave this section of the setup.cfg file empty.
        install_requires_text = ''


    # Initializing the text the program is going to put inside setup.cfg file:
    SETUP_CFG_TEXT = '[metadata]\nname = {package_name}\nversion = {package_version}\nauthor = {author_name}\nauthor_email = {author_email}\ndescription = {description}\nlong_description = file: README.md\nlong_description_content_type = text/markdown\nurl = {url}\nproject_urls =\nBug Tracker = https://github.com/pypa/sampleproject/issues\nclassifiers =\nProgramming Language :: Python :: {python_version}\nLicense :: OSI Approved :: {LICENSE_type} License\nOperating System :: OS Independent\n[options]\npackage_dir =\n = src \npackages = find:\npython_requires = {python_requires}\n{install_requires_text}\n[options.packages.find]\nwhere = src'.format(package_name=package_name,package_version=package_version,author_name=author_name,author_email=author_email,description=description,url=url,python_version=python_version,LICENSE_type=LICENSE_type.upper(),python_requires=python_requires,install_requires=install_requires,install_requires_text=install_requires_text)


    with open("setup.cfg",'w') as f:
        f.write(SETUP_CFG_TEXT)

        print("setup.cgf file created! ")


def add_src_folder(package_name,ignore_list):
    """
    Adds the 'src' folder to root directory
    Adds the 'package_name' folder inside 'src' folder
    Adds the __init__.py file inside 'package_name' folder
    Moving All files (except the ignored ones in 'ignore_list') to 'package_name' folder
    """

    # check if 'src' folder exists, if not create on:
    if not os.path.exists('src'):
        os.mkdir('src')
        print("'src' folder created! ")

    # check if 'package_name' folder exists, if not create one:
    if not os.path.exists(os.path.join('src',package_name)):
        os.mkdir(os.path.join('src',package_name))

        # creats the package folder inside the src
        print("'{}' folder created! ".format(package_name))


    package_name_folder = os.path.join('src',package_name)
    open(os.path.join(package_name_folder,'__init__.py'), 'a').close() # Create __init__.py file in src\\package_name folder
    print("'__init__.py' file created! ")

    # move all the files (except the ignored files) to the package_name folder :

    for file_name in os.listdir():
        if file_name not in ignore_list:
            source = file_name
            destination = os.path.join(package_name_folder,file_name)
            shutil.move(source, destination)
            print(file_name," Moved to: ",destination)

    
def add_tests_folder():
    # check if the directory have this folder ('tests') - if no create one 
    if not os.path.exists('tests'):
        os.mkdir('tests')
        print("'tests' folder created! ")


# ======================== MAIN FUNCTION Of CLI====================


def main():
    """
    CLI in Action
    
    """

    # Start of CLI:

    print("Welcome to HelpMePack - the Python Package Helper CLI ! ")
    print("Please make sure you have your '.git' folder, and README.md, .gitignore, requirments.txt, LICENSE files - in your project directory.")
    print("All the other project files will be moved to the 'src' folder.")
    print("Make sure you running in the Project Main Directory")

    # Initializing the files list to ignore when adding all the package files to 'src' folder

    ignore_list = ['.git','README.md','.gitignore','requirments.txt','LICENSE','src','tests','pyproject.toml','setup.cfg','setup.py']

    # Checks if the package got virtual environment folder, and if so - add it to ignore list

    venv_folder_name = input("Enter the name of this project's Virtual Environment folder: (if it don't have one - press Enter)")
    if venv_folder_name:
        ignore_list.append(str(venv_folder_name))

    # Main CLI action (Getting the info from the user):
    package_name = input("Enter the Package name:")
    package_version = input("Enter the version of the package: (press Enter for Default - 0.0.1)")
    if not package_version:
        package_version = '0.0.1'
    author_name = input("Enter the Author name:")
    author_email = input("Enter the Author Email:")
    description = input("Enter short Description about the package:")
    url = input("Enter the url of the Package (GitHub,GitLab,etc..):")
    python_version = int(float(input("enter Python version: (2 or 3, in form of x.x)")))
    LICENSE_type = input("Enter the LICENSE type: (if you you dont have one just enter the type and the program will add a corresponding license template, press Enter for Default - MIT )").lower()
    python_requires = input("Enter the Python version your package requires: (in form of <=x.x or ==x.x, or >=x.x)")

    # gets from the user the dependencies of his package...
    install_requires = []
    dependency_package = ''
    while dependency_package != 'q':
        
        dependency_package = input("Enter your package dependencies packages names (for example-'requests==2.3.4',gunicorn>=1.0.0','matplotlib<=3.5.1'..)\nwhen you are done enter 'q': ")
        if dependency_package != 'q':
            install_requires.append(dependency_package)
    
    # The HelpMePack program uses the default way of handling packaging in Python - 'src' folder:
    add_src_folder(package_name,ignore_list)

    # adds the mandatory files (with the user info blend in them) to the root directory of the package: 

    add_LICENSE_file(LICENSE_type)
    add_pyproject_file()
    add_README_file(package_name,author_name,description,url,install_requires)
    add_tests_folder()
    add_setup_cfg_file(package_name,package_version,author_name,author_email,description,url,python_version,LICENSE_type,python_requires,install_requires)

    print("Done!")

if __name__ == '__main__':
    main()