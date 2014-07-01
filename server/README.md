pynb server environment
===

### server side extra install:

* conda install ipython, ipython-notebook

* conda install pygments (for nbconvert to html)

* download nodejs from nodejs.org/download, untar into brilconda

    cd $BRILCONDA_HOME
    tar --strip-components 1 -xzf /path/to/node-<blah>.tar.gz   

* build node:
    cd nodexxx
    ./configure
    make 
    make install
    
### nbconvert custom style
    
    ipython nbconvert --template toggle.tpl blah.ipynb
