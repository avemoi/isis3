#!/bin/bash
#
# chmod +x despeckle_start
# ln -s despeckle_start /usr/bin/despeckle
#
# If despeckle runs with parameters --> fires the commandline script
# if no parameters --> GUI is started 
#
installation_path="/opt/Despeckle_pyqt/"
desp="Despeckle/a_despeckle.sh"
desqt="py_src/despeckle_main.py"
execpath=$installation_path$desqt
 
echo "number of parameters $#"
	if [ $# -eq 0 ]
	then
		#python $installation_path$despeckle_main
		python $execpath
	elif [  $# -lt 3  -o $# -gt 7 ]
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
        
        echo $1
		echo $2
		echo $3
		echo $4
		echo $5
		echo $6
		echo $7
		
		sh $installation_path$desp $1 $2 $3 $4 $5 $6 $7
        
	fi
