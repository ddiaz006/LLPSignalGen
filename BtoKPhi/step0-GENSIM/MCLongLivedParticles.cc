
#include "GeneratorInterface/GenFilters/interface/MCLongLivedParticles.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include <iostream>

using namespace edm;
using namespace std;


MCLongLivedParticles::MCLongLivedParticles(const edm::ParameterSet& iConfig) :
  token_(consumes<edm::HepMCProduct>(iConfig.getParameter<edm::InputTag>("hepMCProductTag"))) {
  //here do whatever other initialization is needed
  //theCut = iConfig.getUntrackedParameter<double>("LengCut",10.);
  }


MCLongLivedParticles::~MCLongLivedParticles()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


// ------------ method called to skim the data  ------------
bool MCLongLivedParticles::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  using namespace edm;
  
  Handle<HepMCProduct> evt;
  
  iEvent.getByToken(token_, evt);
  //iEvent.getByLabel(hepMCProductTag_, evt);
  
  bool pass = false;
  
  const HepMC::GenEvent * generated_event = evt->GetEvent();
  HepMC::GenEvent::particle_const_iterator p;
  
  for (p = generated_event->particles_begin(); p != generated_event->particles_end(); p++) { 
  
    //cout << "particle : " << (*p)->pdg_id() << "\n";
    if (abs((*p)->pdg_id() == 9900015)) {
      cout << "found LLP\n";
      if ((*p)->end_vertex()) {
	double z = ((*p)->end_vertex())->position().z();
	double r = sqrt( ((*p)->end_vertex())->position().x() * ((*p)->end_vertex())->position().x()
			 + ((*p)->end_vertex())->position().y() * ((*p)->end_vertex())->position().y() );
	double eta = (*p)->momentum().eta();
	double pt = sqrt( (*p)->momentum().px()*(*p)->momentum().px() + (*p)->momentum().py()*(*p)->momentum().py());
	
	cout << pt << " " << z << " " << r << " " << eta << " \n";
	bool isCSC = (fabs(z) > 4000 && fabs(z) < 11000 && r < 6955);
	bool isDT = (fabs(z) < 6610 && r > 2000 && r < 8000.0 );
	bool inMSAcceptance = (!(fabs(z) < 4000 && r < 2000) && fabs(z) < 12000 && r < 8000);
	
	if ( inMSAcceptance && fabs(eta) < 4.0 ) {
	  pass = true;
	}
	cout << "pass = " << pass << "\n";
      } else {
	cout << "no end_vertex found\n";
      }
    }
  }
  
  


  return pass;
}

