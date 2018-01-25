This folder is where we run our implementation.
Each of the .cmd files are used to execute specific commands.
        test-6k.cmd -   Used to test the predictions of the network trained on 23 classes, using the 6k dataset. The network used is NETWORK 3 (stage 2) mentioned in the pdf.
                        Threshold is set to 25%, and can be changed in the cmd file.
                        Make sure to change the path of the image file to be tested in this cmd file.
        test-608.cmd -  Used to test the predictions of the network trained on 23 classes, using the 6k dataset. The network used is NETWORK 1 (stage 2) mentioned in the pdf.
                        Threshold is set to 25%, and can be changed in the cmd file.
                        Make sure to change the path of the image file to be tested in this cmd file.
        test-bv.cmd -   Used to test the predictions of the network trained on 1 class, using the 200k dataset. The network used is NETWORK 3 (stage 1) mentioned in the pdf.
                        Threshold is set to 25%, and can be changed in the cmd file.
                        Make sure to change the path of the image file to be tested in this cmd file.

        train-6k.cmd -  Used to train the stage 2 of NETWORK 3 on 6k image dataset.
        train-608.cmd - <Training for NETWORK 1, as mentioned in the pdf, is done on flux. The command is similar to that of 6k>.
        train-bv.cmd -  Used to train the stage 1 of NETWORK 3 on 200k image dataset.

        valid-6k.cmd -  Used to test the predictions of the final output of NETWORK 3 trained on 23 classes, using the 6k dataset.
                        Output is stored in ./results/ as a text file names 'r599-detection.txt'
                        Threshold can be changed in the cmd file.
                        The list of text files are provided in the ./data/obj.data file under variable 'valid'.
        valid-608.cmd - Used to test the predictions of the network trained on 23 classes, using the 6k dataset.
                        Output is stored in ./results/ as a text file names 'r599-detection.txt'
                        Threshold can be changed in the cmd file.
                        The list of text files are provided in the ./data/obj.data file under variable 'valid'.
        valid-bv.cmd -  Used to test the predictions of the output of stage 1 of NETWORK 3 trained on 1 class, using the 200k dataset.
                        Output is stored in ./results/ as a text file names 'r599-detection.txt'
                        Threshold can be changed in the cmd file.
                        The list of text files are provided in the ./data/bv.data file under variable 'valid'.

Order of files in this folder:
	backup/		- contains the weights files.
	cfg/		- contains the .cfg files for the networks.
	data/		- contains the .data files and .names files for the networks.
	Release/	- contains object files for knights.exe
	results/	- contains the output text files as a list, for the images used to test as a batch.
	knights.exe	- executable file
	knights.iobj	- IOBJ file
	knights.ipdb	- IPDB file
	knights.pdb	- PDB file
	opencv_world320.dll - extension
	predictions.jpg - output image file with bounding box
	pthreadVC2.dll	- extension
	Readme_x64.txt
	(list of .cmd files)