dirCentral=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/BtoKPhi/step3-RECO
dirWorking=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_6_17_patch1/src/

for file in $dirCentral/*cfg.py
do
  ln -s $file $dirWorking
done

ln -s ${dirCentral}/multi_crab_submit_step3_RECOSIM.py $dirWorking
