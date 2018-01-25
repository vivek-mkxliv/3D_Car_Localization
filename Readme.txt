==================================================================================================
==================================================================================================
Course	: ROB 599 - Self Driving Vehicles
Term	: Fall 2017
Project	: Final_Perception
Team	: Team 2 - Knights Who Say Ni (a.k.a. Knights)
==================================================================================================
==================================================================================================

Readme.txt
==================================================================================================
Contents :
	1. Preparing the datasets
		a. 200k Dataset
		b. Deploy
	2. Knights - the executable file
	3. Create 3D_bboxes from 2D_data
	4. Evaluation script
==================================================================================================

==================================================================================================
SOFTWARES AND TOOLS USED
	1. Platform (OS): Windows 10
	2. IDE		: Windows MS Visual Studio 2015 (v140)
	3. Python	: v3.5.2
	4. Python Dependencies:	
	5. OpenCV	: v3.0
	6. CUDA		: 9.0
	7. cuDNN	: 7
	8. System Specs	: Alienware 15R3; intel i7; RAM 16GB DDR4; NVIDIA GeForce GTX1060 8GB
	9. Link to our weight files : https://drive.google.com/drive/folders/1H_DIBL8LYv3ZVZi1XpSa7QmZPUl5I_sg?usp=sharing
==================================================================================================

==================================================================================================
.zip file contains:
	./3dbbox
	./200k dataset - DROP Lab
	./deploy
	./eval
	./Knights
	Readme.txt
	ROB599_Team2_Knights.pdf
==================================================================================================

P.S. : Windows was not able to read relative paths, so please change the paths to all the lines as specified in the respective python codes below (i.e., full paths).

==================================================================================================
1. PREPARING THE DATASETS
	We used two datasets for the training process.
		i.  Dataset from DROP Lab - Driving in the Matrix - repro_200k. (will be referred to as 200k)
		    Download links available at : "https://fcav.engin.umich.edu/sim-dataset"
		ii. Given dataset with 6k images under "rob599_dataset_deploy/trainval/.." (will be referred to as 6k)
		    Download link available in the project description pdf.
	For testing, we used the given test dataset under "rob599_dataset_deploy/test/.."

	We restructured the datasets and created "test.txt", "train6k.txt", and "train200k.txt" to train our networks with the process described below.
	Python codes required:
		./Team 2 - Knights/200k dataset - DROP Lab/data-label.py
		./Team 2 - Knights/deploy/input_bbox.py
		./Team 2 - Knights/deploy/train_structure.py
		./Team 2 - Knights/deploy/test_structure.py

		(more information is specified in the individual radme text files under each folder)

	200k training dataset processing:
		Download the 200k images, 200k annotations, 200k Image Sets, and 200k pixel level segmentation images from the download link.
		Extract the data to "./Team 2 - Knights/200k dataset - DROP Lab/"
		The folder should now contain a folder named "VOC2012".
		Run the  "./Team 2 - Knights/200k dataset - DROP Lab/data-label.py" file.
			Change the path in line 7 of the code to "/full/path/to/VOC2012"
		This code generates labels as .txt files for each image and places them under "./Team 2 - Knights/Team 2 - Knights/200k dataset - DROP Lab/VOC2012/labels/.."
		The code will also generate a "train200k.txt" file under "./Team 2 - Knights/200k dataset - DROP Lab/" that specifies a list of paths to all the 200k images.

	Deploy - 6k training dataset processing:
		Download the provided dataset from the download link.
		Extract the contents ("./test/" and "./trainval/") to the ./Team 2 - Knights/deploy/ folder.
		The "deploy" folder should now contain folders named "test" and "trainval".
		Run the  ./Team 2 - Knights/deploy/input-bbox.py file to generate 2D bounding box labels as a text file from the provided 6k dataset.
			Change the path in line 5 of the code to /full/path/to/deploy/trainval/
			This code generates labels as .txt files for each image and places them under the respective images.
		Run the ./Team 2 - Knights/deploy/train_structure.py
			Change the paths in line 13 to /full/path/to/deploy/
			Change the paths in line 14 to /full/path/to/obj/
			Change the paths in line 15 to /full/path/to/train6k.txt
			This code restructures the 6k trainval images and respective labels to ./Team 2 - Knights/deploy/obj/ folder.
			The code will also generate a train6k.txt file under ./Team 2 - Knights/deploy/ that specifies a list of paths to all the 6k images.

	Deploy - test dataset processing:
		Download the provided dataset from the download link.
		Extract the contents ("./test/" and "./trainval/") to the ./Team 2 - Knights/deploy/ folder.
		The "deploy" folder should now contain folders named "test" and "trainval".
		Run the ./Team 2 - Knights/deploy/test_structure.py
			Change the paths in line 13 to /full/path/to/deploy/
			Change the paths in line 14 to /full/path/to/deploy/
			This code restructures the 2k test images and respective labels to ./Team 2 - Knights/deploy/testimages/ folder.
			The code will also generate a test.txt file under ./Team 2 - Knights/deploy/ that specifies a list of paths to all the test images.

	(We included the "test.txt", "train6k.txt", and "train200k.txt" files in the .zip so that you can see the structure of these files. But they have to be re-generated because the paths will be different.)	

==================================================================================================

2. KNIGHTS
	The training procedure is specified in the pdf. (Refer to pdf about the 3 networks).

	Download link to the final weight files for the 3 networks we trained : https://drive.google.com/drive/folders/1H_DIBL8LYv3ZVZi1XpSa7QmZPUl5I_sg?usp=sharing
		(Anyone with a umich gmail id with this link can access the weights file)
		Extract the "backup" folder in the provided link to ./Team 2 - Knights/Knightsbuild/knights/x64/ folder.

	Copy and paste all the "test.txt", "train6k.txt", and "train200k.txt" files generated in the previous step to ./Team 2 - Knights/Knightsbuild/knights/x64/data/ folder.
		(We included these files in the .zip so that you can see the structure of these files. But they have to be re-generated because the paths will be different.)

	Each of the .cmd files specified in the ./Team 2 - Knights/Knightsbuild/knights/x64/ are used to execute specific commands of the network.
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
	                        Output is stored in "./Team 2 - Knights/Knightsbuild/knights/x64/results/" as a text file names "r599-detection.txt"
        	                Threshold can be changed in the cmd file.
	                        The list of text files are provided in the "./Team 2 - Knights/Knightsbuild/knights/x64/data/data/obj.data" file under variable 'valid'.
	        valid-608.cmd - Used to test the predictions of the network trained on 23 classes, using the 6k dataset.
        	                Output is stored in "./Team 2 - Knights/Knightsbuild/knights/x64/results/" as a text file names "r599-detection.txt"
                	        Threshold can be changed in the cmd file.
                        	The list of text files are provided in the "./Team 2 - Knights/Knightsbuild/knights/x64/data/data/obj.data" file under variable 'valid'.
	        valid-bv.cmd -  Used to test the predictions of the output of stage 1 of NETWORK 3 trained on 1 class, using the 200k dataset.
        	                Output is stored in "./Team 2 - Knights/Knightsbuild/knights/x64/results/" as a text file names "r599-detection.txt"
                	        Threshold can be changed in the cmd file.
                        	The list of text files are provided in the "./Team 2 - Knights/Knightsbuild/knights/x64/data/bv.data" file under variable 'valid'.

	Order of files in this folder:
		backup/		- contains the final weights files used for the 3 networks we trained on.
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

	For the testing, we can use the "test-*.cmd" files for a single image output, or "valid-*.cmd" files for a batch process.
	The "./Team 2 - Knights/Knights/build/knights/x64/results/" folder contains a text file named "r599-detection.txt", which gives the output of the network, when ran  on the test images in batch mode.
		This is done using the valid-*.cmd files mentioned above.
		(An example of "r599-detection.txt" file is included in the .zip, but it will have to be regenerated because of the change in paths)

	This "r599-detection.txt" has all the predictions made by the network for each image in the format :
		path/to/testimages/guid_*.jpg, class id, x, y, w, h, conf
		where the values of x, y, w, h are in pixels. conf is in percentage.

==================================================================================================

3. CREATE 3D_BBOXES FROM 2D_DATA	
	Python codes required:
		./Team 2 - Knights/3dbbox/3D_bounding_box.py
		./Team 2 - Knights/3dbbox/3d_support_script.py

	Copy and paste the "./Team 2 - Knights/Knights/build/knights/x64/results/r599-detection.txt" generated in the previous step to "./Team 2 - Knights/3dbbox/" folder.
	Run the ./Team 2 - Knights/3dbbox/3d_support_script.py code to make some small changes in the text file that is required to proceed with our further code.
		Change the path in line 3 to the full path that specifies "./Team 2 - Knights/3dbbox/" folder.
		Only one aspect of the path of the image is changed. Everything else remains the same.
		This code gives a new text file by the name "r599-detection-v2.txt".
		(An example of "r599-detection-v2.txt" file is included in the .zip, but it will have to be regenerated because of the change in paths)

	Run the  "./Team 2 - Knights/3dbbox/3D_bounding_box.py" code to generate the 3D bounding box data using the x, y, w, h generated in the previous step.
		Change the path in line 36 to the full path that specifies "./Team 2 - Knights/3dbbox/r599-detection-v2.txt" file.
		Change the path in line 170 to the full path that specifies "./Team 2 - Knights/3dbbox/" folder.
		This code gives a new text file by the name "r599-detection-3d-bbox.txt", that contains predictions made by the network in 3d, in the format:
		path/to/test/guid_*.jpg, class id, x, y, z, l, w, h, conf
		where the values of x, y, z, l, w, h are in meters. conf is in percentage.
		(An example of "r599-detection-3d-bbox.txt" file is included in the .zip, but it will have to be regenerated because of the change in paths)

==================================================================================================

4. EVALUATION
	Python codes required:
		./Team 2 - Knights/eval/eval_script.py

	Copy and paste the "./Team 2 - Knights/3dbbox/r599-detection-3d-bbox.txt" generated in the previous step to "./Team 2 - Knights/eval/" folder.
	Run the ./Team 2 - Knights/eval/eval_script.py code to make some small changes in the text file that is required to proceed with our further code.
		Change the path in line 72 to the full path that specifies "./Team 2 - Knights/eval/" folder.
		Only one aspect of the path of the image is changed. Everything else remains the same.
		This code gives a new text file by the name "final_result_3d.txt", that gives us the final result (the text file that we uploaded to kaggle)
		(An example of "final_result_3d.txt" file is included in the .zip, but it will have to be regenerated because of the change in paths)

==================================================================================================