if __name__ == '__main__':

    #filter efficiency

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
    config.JobType.pluginName = 'PrivateMC'
    config.JobType.eventsPerLumi = 1000 #200
    config.JobType.maxJobRuntimeMin = 2750

    config.section_("Data")
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 200000 #500000 #gen filter efficiency is 6e-4, so 100K will give 60 events output
    config.Data.totalUnits = 2000000000 #5000000
    #config.Data.unitsPerJob = 1000 
    #config.Data.totalUnits = 10000000
    config.Data.publication = True
    #config.Data.publication = False
  
    config.section_("Site")
    #config.Site.storageSite = 'T2_US_Caltech_Ceph'
    #config.Site.storageSite = 'T3_US_FNALLPC'
    config.Site.storageSite = 'T2_US_UCSD'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

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

    #mode_list = ["BToKPhi_MuonLLPDecayGenFilter_PhiToPi0Pi0"]
    mode_list = ["BToKPhi_MuonLLPDecayGenFilter_PhiToPiPlusPiMinus"]
    #mode_list = ["BToKPhi_MuonGenFilter_PhiToPiPlusPiMinus"]



    ms_list = ["3p0"]
    pl_list = ["3000"]
    batch="batch4"
    pset_dir = "/afs/cern.ch/work/d/ddiaz/LLPSignalGen/CMSSW_10_2_27/src/"
    for i in range(len(mode_list)):
	mode = mode_list[i]
	for ms in ms_list: 
	    for pl in pl_list:
                spec = mode+"_mPhi{}_ctau{}".format(ms,pl)
                #spec = mode+"_GenOnly_mPhi{}_ctau{}".format(ms,pl)
		
                config.General.requestName = 'Ul18_'+mode+"_mPhi{}_ctau{}".format(ms,pl)+'_GENSIM_'+batch
		config.Data.outputPrimaryDataset = spec
                #config.Data.outLFNDirBase = '/store/group/lpclonglived/apresyan/privateProduction/GS/RunIIFall18_test/GENSIM/' + mode + "_mPhi{}_ctau{}".format(ms,pl) + "/batch2/"
                #config.Data.outLFNDirBase = '/store/group/LLPs/BtoKPhiSamples/privateProduction/GS/' + mode + "_mPhi{}_ctau{}".format(ms,pl) + "/"+batch+"/"
                config.Data.outLFNDirBase = '/store/group/LLPs/BtoKPhiSamples/privateProduction/GS/'

                config.JobType.psetName = pset_dir + "/" + mode + "_mPhi{}_ctau{}_LLPDecayFilter_cfg.py".format(ms,pl)
                #config.JobType.psetName = pset_dir + "/" + mode + "_mPhi{}_ctau{}_cfg.py".format(ms,pl)

		config.JobType.numCores = 1
		print 'config %s' %(config.JobType.psetName)
		print 'output %s' %(config.Data.outLFNDirBase)
		submit(config)
