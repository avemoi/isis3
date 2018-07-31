#!/bin/bash
#
# Usage :
# 
# sh despeckle.sh input_image kernel.txt   (with default values l=0.08, iterations=100)
#
# sh despeckle.sh input_image kernel.txt output_path -l l_value -i number_of_iterations
#
#
img_input_original=$1
kernel_input_original=$2
img_output_path=$3
img_name=$img_input_original
img_input_original=`realpath $img_input_original`
kernel_input_original=`realpath $kernel_input_original`

prep_path=""
output_directory=""
temp_dir=/tmp/isis3_despeckle/

# default values
l_value=0.08
iterations=100

check_exit() {

if [ $? -ne 0 ]
then
    echo "error"
fi

#san exceptions handle errors!!!
#  
#    error logs   FILE **********************

}
#
clean_files()      {
    
    #shopt -s extglob
    
    #rm !(final_despeckled_image.cub|$kernel_input_original|$img_input_original)
    
    #rm a.cub
    #rm b.cub
    #rm c.cub
    #rm final.cub
    #rm mask.cub
    #rm output.cub
    #rm output0.cub
    #rm output2.cub
    #rm prep.cub
    #rm temp_image.cub
    #rm temp_image_input.cub
	rm $temp_dir/*
    
}






despeckle() {

	img_input=$1
	temp_dir=$2
	
	echo "L IS  $l_value"
	echo "iterations are $iterations"
	l=$(bc <<< "1 - $l_value")
	
	
	
	cat $img_input > $temp_dir/temp_image_input.cub
	
#set null pixels equal to 0
	stretch from=$temp_dir/temp_image_input.cub to=$temp_dir/temp_image.cub null=0 lis=0 lrs=0 his=0 hrs=0	

	temp=$temp_dir/temp_image.cub

	fx F1=$temp_dir/temp_image.cub TO=$temp_dir/output0.cub equation=F1*$l_value
	echo "L*img OUT OF THE LOOP"

	i=1
	while [ "$i" -le $iterations ] 
	do 
  #echo "start while"
	echo "Iteration $i"
	printf "\n"
	
	#dimiourgei plaisio Null timwn eurous 1 gurw apo tin eikona
		pad from=$temp to=$temp_dir/a.cub left=1 right=1 top=1 bottom=1
	
	#dinei tin timi 0 gurw sta null pixels gurw apo tin eikona
		stretch from=$temp_dir/a.cub to=$temp_dir/b.cub null=0
	
	#pernaei to filtro
     kernfilter FROM=$temp_dir/b.cub TO=$temp_dir/c.cub KERNEL=$kernel_input_original
                
  
	#meta to perasma tou filtrou apokoptonte oi perimetrikes times kai pernoun tin timi null
	#opote apokovoume aftes tis times kai epistrefoume stin arxiki diastasi tou cub
	cropspecial from=$temp_dir/c.cub to=$temp_dir/output.cub


    echo "imgKER*(1-l)"
    fx F1=$temp_dir/output.cub TO=$temp_dir/output2.cub equation=F1*$l


    echo "L*img+(1-L)*imgKER"
	fx F1=$temp_dir/output2.cub F2=$temp_dir/output0.cub TO=$temp_dir/final.cub equation=F1+F2


	temp=$temp_dir/final.cub

	i=$(($i+1)) 
	printf "\n\n"
	done



	stretch from=$img_input_original to=$temp_dir/mask.cub lis=null lrs=null his=null hrs=null

	mask from=$temp_dir/final.cub mask=$temp_dir/mask.cub to=$temp_dir/final_image.cub	
	
	mv $temp_dir/final_image.cub $output_directory
	#mv $temp_dir/final_image.cub $final_path
	#mv $output_directory/final_image.cub  $output_directory/$img_name
	#img_name


	#############################
	#							#
	#SUBSTR FOR INPUT IMAGE NAME#
	#							#
	#############################









}






valueToFloat()  {
# change all values to float 
# in case there is an attribute in
# scientific notation (bc error).
    printf '%4.17f' $1
}





get_statistics() {

    
    img_avg=`stats FROM=$img_input_original | grep Average | sed -e 's/^[^=]*=//g' |  sed -e 's/^[ \t]*//' `

    #pairnw to StandardDeviation, apomonwnw ton arithmo mono kai to pros8etw sto arxeio Stats.txt
    img_std=`stats FROM=$img_input_original| grep StandardDeviation | sed -e 's/^[^=]*=//g' | sed -e 's/^[ \t]*//' `

    #pairnw to maximum, apomonwnw ton arithmo mono kai to pros8etw sto arxeio Stats.txt
    img_max=`stats FROM=$img_input_original| grep -w Maximum | sed -e 's/^[^=]*=//g' | sed -e 's/^[ \t]*//' `

    #pairnw to minimum, apomonwnw ton arithmo mono kai to pros8etw sto arxeio Stats.txt
     img_min=` stats FROM=$img_input_original| grep -w Minimum | sed -e 's/^[^=]*=//g' | sed -e 's/^[ \t]*//' `
    
    #echo "avg $img_avg"
    #echo "std $img_std"
    #echo "max $img_max"
    #echo "min $img_min"
}





median_apply() {

# convert values
img_std=`valueToFloat $1`
img_avg=`valueToFloat $2`
img_max=`valueToFloat $3`
img_min=`valueToFloat $4`
temp_dir=$5

#pre-processing image using"
#k = mean(Img) + 3*std(Img)"
#use of median, we keep as valid only values from 0 to k, everything else median 5x5"
#
# 4 * StandardDeviation(img)

res_std=$(bc <<< "$img_std * 4")

# compute k
k=$(bc <<< "$img_avg + $res_std")


#upologismos a,b
val=0.000000000001
a=$(bc <<< "$img_max + $val")
b=$(bc <<< "$img_min- $val")


echo "min= $img_min"
echo "max= $img_max"
echo "std= $img_std"
echo "avg= $img_avg"

echo "resstd= $res_std"
echo "k =$k"
echo "a=$a"
echo "b=$b"


#efarmogh media se ola ektos ap auta poy briskontai metaksy 0 kai K
#xwris ta special pixels

prep_name="prep.cub"
prep_path=$temp_dir$prep_name
#echo $prep_path

median FROM=$img_input_original to=$prep_path samples=9 lines=9 low=$k high=$a hrs=no his=no lrs=no lis=no null=no filter=inside


#median FROM=prep.cub to=prepared_image.cub samples=9 lines=9 low=$b high=0.000000000000001 hrs=no his=no lrs=no lis=no null=no filter=inside
##### ERROR to "LOW" einai megalytero toy HIGH


}









echo "number of parameters $#"
    if [  $# -lt 3  -o $# -gt 7 ]
    then
        echo "Usage: despeckle img.cub kernel.txt output_path [-OPTION] [VALUE]"
        echo "Try 'RTFM' for more information."
            
    else
        # in order to skip the first argument (kernel)
        OPTIND=4
        while getopts "i:l:" opt
        do
        
            case "$opt" in
                i) echo "found the -i option with value $OPTARG"
                   if [ $OPTARG -lt 1 ] 
                   then
                       echo "Acceptable values for iterations are 0..n, exiting"
                       exit -1
                   else
                       iterations=$OPTARG
                   fi
                    ;;
                   
                l) echo "found the -l option with value $OPTARG"
                   if (( $(echo "$OPTARG > 1" | bc -l) || $(echo "$OPTARG < 0" | bc -l) ))
                   then
                        echo "Acceptable values for l parameter are 0..1, exiting"
                        exit -1
                   else
                        l_value=$OPTARG
                    fi
                    ;;
                *) echo "unknown option: $opt";;
            esac
        done
        
        
        #user=`whoami`
        
        
        #if [ -z "$3" ] 
        #then
        	#	output_directory=/home/$user/	
        #else
        	# 	output_directory=$3
    	#fi
        
        output_directory=$3
        
        if [ ! -d "$temp_dir" ]; then
			mkdir $temp_dir
		fi
   
		echo $1
		echo $2
		echo $3
		echo $4
		echo $5
		echo $6
		echo $7
		echo $8
        
        ##################################
		#check for rw permissions        #
		#check if exists --> replace file#
		##################################
        
		#echo $img_name
        
        get_statistics 
        
    	median_apply  $img_std $img_avg $img_max $img_min $temp_dir
        
        despeckle $prep_path $temp_dir
        
        clean_files
        
        #mv final_image.cub final_$img_input_original
    fi

     

     




