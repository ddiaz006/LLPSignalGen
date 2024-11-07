dirCentral=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/BtoKPhi/step1-PU
dirWorking=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_6_17_patch1/src/

for file in $dirCentral/*cfg.py
do
  ln -s $file $dirWorking
done

ln -s ${dirCentral}/multi_crab_submit_step1.py $dirWorking
