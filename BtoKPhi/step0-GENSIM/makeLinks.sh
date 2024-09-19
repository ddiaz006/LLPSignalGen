dirCentral=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/BtoKPhi/step0-GENSIM
dirWorking=/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_2_27/src/

for file in $dirCentral/*cfg.py
do
  ln -s $file $dirWorking
done

ln -s ${dirCentral}/multi_crab_submit_BToKS_step0.py $dirWorking
