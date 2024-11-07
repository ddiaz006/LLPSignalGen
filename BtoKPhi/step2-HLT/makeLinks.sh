dirCentral=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/BtoKPhi/step2-HLT
dirWorking=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_2_16_UL/src/

for file in $dirCentral/*cfg.py
do
  ln -s $file $dirWorking
done

ln -s ${dirCentral}/multi_crab_submit_step2.py $dirWorking
