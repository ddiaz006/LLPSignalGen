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
    config.JobType.psetName = '/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_6_17_patch1/src/step1_cfg.py'
    #config.JobType.numCores = 1
    config.section_("Data")

    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'Automatic'  #'FileBased'

    #For QCD GEN-SIM samples
    #config.Data.inputDBS = 'global'
    #config.Data.splitting = 'LumiBased'
    #config.Data.lumiMask = 'my_lumi_mask_batch5.qcd.json'

    config.Data.unitsPerJob = 181 #1 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = True

    config.section_("Site")
    #config.Site.storageSite = 'T3_US_FNALLPC'
    config.Site.storageSite = 'T2_US_UCSD'
    #config.Site.storageSite = 'T2_US_Caltech_Ceph'
    config.Site.whitelist = ['T2_US_*','T3_US_FNALLPC']
    #config.Site.whitelist = ['T2_US_Caltech']
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
#Command to get the dictionary from crab log
#cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"Fall18_DR_step1_"$2"_batch1_v1\","}'
# /BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau300/LLPs-crab_Ul18_BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau300_GENSIM_batch3-e45192c9b89d03ee1db662cee489dd46/USER
    datasetToNameDict = {                  
                  
    
"/BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000/LLPs-crab_Ul18_BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000_GENSIM_batch4-e45192c9b89d03ee1db662cee489dd46/USER":"UL18_DR_step1_BToKPhi_MuonGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000_batch4_v1",

        #Did not submit below      
     
       
      
    
        }

#Command to get the dictionary from crab log

#cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"/store/group/lpclonglived/apresyan/privateProduction/DR/step1/RunII_UL18/GENSIM/"$2"/batch1/v1/\","}'


    datasetToOutput = {       
        
       "/BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000/LLPs-crab_Ul18_BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000_GENSIM_batch4-e45192c9b89d03ee1db662cee489dd46/USER":"/store/group/LLPs/BtoKPhiSamples/privateProduction/DR/step1/UL18_DR_step1_BToKPhi_MuonGenFilter_PhiToPiPlusPiMinus_mPhi0p3_ctau3000/batch4/",

        #Did not submit below       

   
     
        }


    for dataset in datasetToNameDict :
        name = datasetToNameDict[dataset]
        output = datasetToOutput[dataset]

        config.General.requestName = name
        config.Data.inputDataset = dataset
        config.Data.outLFNDirBase = output

        config.JobType.numCores = 8
        config.JobType.maxMemoryMB = 16000
        print(config.General.requestName)
        print(config.Data.inputDataset)
        print(config.Data.outLFNDirBase)
        submit(config)

