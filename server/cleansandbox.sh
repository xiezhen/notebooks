#!/bin/bash
sandboxdir=/home/zhen/work/pynb/sandbox
if [ -d $sandboxdir ]; then
   workdir=`pwd`
   cd $sandboxdir
   for i in `ls -A`; do if [ -d $i ]; then rm -rf $i; fi; done
   cd $sandboxdir  
fi
