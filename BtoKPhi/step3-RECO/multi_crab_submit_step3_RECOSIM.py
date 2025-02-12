if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    #from CRABClient.UserUtilities import config
    #config = config()
    from WMCore.Configuration import Configuration
    config = Configuration()

    config.section_("General")
    config.General.workArea = 'crab'
    config.General.transferOutputs = True
    config.General.transferLogs = False

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = '/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_6_17_patch1/src/step3_RECO_cfg.py'
    config.JobType.numCores = 1
    config.section_("Data")
    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 1 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = True
    #config.Data.lumiMask = 'my_lumi_mask_batch1_part2.json'

    config.section_("Site")
    #config.Site.storageSite = 'T2_US_Caltech_Ceph'
    config.Site.storageSite = 'T2_US_UCSD'
    config.Site.whitelist = ['T2_US_*', 'T3_US_FNALLPC']
    config.Site.ignoreGlobalBlacklist = True
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
#cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"UL18_DR_step3_"$2"_batch1_v1\","}'

    datasetToNameDict = {               
      
        "/BToKPhi_MuonGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau300/LLPs-crab_UL18_DR_step2_BToKPhi_MuonGenFilterOnly_PhiToPiPlusPiMinus_mPhi0p3_ctau300_batch4_v1-b403a189a2d057e62e59ed092120c7f4/USER":"UL18_DR_step3_BToKPhi_MuonGenFilterOnly_PhiToPiPlusPiMinus_mPhi0p3_ctau300_batch4_v1",

        #below not submitted yet       
        }

  
   #cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"/store/group/lpclonglived/apresyan/privateProduction/DR/step3_RECOSIM/RunII_UL18/"$2"/batch1/v1/\","}'

    datasetToOutput = {       
        "/BToKPhi_MuonGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau300/LLPs-crab_UL18_DR_step2_BToKPhi_MuonGenFilterOnly_PhiToPiPlusPiMinus_mPhi0p3_ctau300_batch4_v1-b403a189a2d057e62e59ed092120c7f4/USER":"/store/group/LLPs/BtoKPhiSamples/privateProduction/DR/step3/UL18_DR_step3/UL18_DR_step3_BToKPhi_MuonGenFilterOnly_PhiToPiPlusPiMinus_mPhi0p3_ctau300/batch4/",

        #below not submitted yet 
      

    }


    for dataset in datasetToNameDict :
        name = datasetToNameDict[dataset]
        output = datasetToOutput[dataset]

        config.General.requestName = name
        config.Data.inputDataset = dataset
        config.Data.outLFNDirBase = output

        config.JobType.maxMemoryMB = 3000
        print(config.General.requestName)
        print(config.Data.inputDataset)
        print(config.Data.outLFNDirBase)
        submit(config)

 
