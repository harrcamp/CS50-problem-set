import pandas as pd

# Email addresses provided by the user
email_list = """
salesteam@nagarro.com david.dawson@nagarro.com campaigns@nagarro.com peter.harder@nagarro.com ravi.dhingra@nagarro.com dmitry.lopatik@nagarro.com alexandra.kissinger@nagarro.com kapil.ahuja@nagarro.com ajit.appachu@nagarro.com challapalli.vamshi@nagarro.com chittaranjan.jena@nagarro.com deepakn@nagarro.com cristian.mesaros@nagarro.com kaytor.tuan@nagarro.com david.marchand@nagarro.com deepak.menghani01@nagarro.com bjarne.moberg@allgeier-es.com michael.moller@nagarro.com catalin.busneag@nagarro.com eric.bartels@nagarro.com sunil.kanderi@nagarro.com sanya.samant@nagarro.com ram.reddy01@nagarro.com julia.durow@nagarro.com jim.thill@nagarro.com dan.tusaliu@nagarro.com ludwig.bruennig@nagarro.com martin.schweinberger@nagarro.com joanna.horn@nagarro.com csaba.szabo@nagarro.com neelanchi.verma01@nagarro.com kim.cook@nagarro.com martin.hack@nagarro.com matt.pierce@nagarro.com joerg.dietmann@nagarro.com bernd.schulze@nagarro.com dan.kehoe@nagarro.com paul.haberfellner@nagarro.com joe.toste@nagarro.com frederik.sahlin@nagarro.com holger.kuhfuss@nagarro.com vera.reichlin-meldegg@nagarro.com travis.williams@nagarro.com kapil.bhatia@nagarro.com divya@nagarro.com charu01@nagarro.com gustav.manding@nagarro.com harsh.narula@nagarro.com andrea.rath-rauch@nagarro.com ben.ziff@nagarro.com kathleen.hannon@nagarro.com surya.vedula@nagarro.com rodrigo.cruz@nagarro.com michael.corrigan@nagarro.com wolfgang.bauer@nagarro.com marius.schmelcher@nagarro.com bachar.kassar@nagarro.com toshi.yamanouchi@nagarro.com marius.luca@nagarro.com sebastian.gesellensetter@nagarro.com charley.mitchell@nagarro.com yogi.misir@nagarro.com stefan.rother@allgeier-es.com joos.cadonau@nagarro.com bjarne.moberg@nagarro.com kapil@nagarro.com jennifer.schwalbenbach@nagarro.com kelsey.samson@nagarro.com ionut.pop@nagarro.com pankaj.gupta04@nagarro.com syed.ahamed@nagarro.com katie.mcvay@nagarro.com peter.hammer@nagarro.com kunal.mathur@nagarro.com susanne.soumelidis@nagarro.com bernd.ruiss@nagarro.com christoph.reissner@nagarro.com manas@nagarro.com hannes.faerberboeck@nagarro.com pragathi.kanth@nagarro.com ananda.sengupta@nagarro.com alexander.lindner@nagarro.com tarun.madan@nagarro.com thomas.aardal@nagarro.com andreea.goia@nagarro.com bharat.sharma01@nagarro.com elisabeth.schweighofer@nagarro.com saumya.tripathi@nagarro.com amar.chandani@nagarro.com joey.silverain@nagarro.com troy.quillen@nagarro.com martin.reinke@allgeier-es.com andreas.chaloupka@nagarro-es.com peter.kuras@nagarro.com avinash.shukla@nagarro.com eddie.tasbas@nagarro.com sumitra.ayyangar@nagarro.com rishiraj.ranga@nagarro.com nainy.katyal@nagarro.com parveen.gulia@nagarro.com chinmaya.nayak@nagarro.com pramod.pandey@nagarro.com amaan.rahman@nagarro.com matthias.krefeld@nagarro-es.com julia.rettig@nagarro.com stefan.schwartz@nagarro.com patrick.riedl@nagarro.com helene.schneider@nagarro.com christian.mommsen@nagarro.com carl.lucas@nagarro.com wolfgang.froehlich@nagarro.com markus.gniech@nagarro-es.com leslie.james@nagarro.com rajiv.sharma@nagarro.com samruddhi.puranik@nagarro.com neil.morecraft@nagarro.com gtm@nagarro.com pooja.kishore@nagarro.com laudine.fauconet@nagarro.com pascal.cuzon@nagarro.com pascal.cuzon@nagarro-es.com alexander.boehm@nagarro.com stefan.baer@nagarro.com shubham.kohli@nagarro.com alexandra.kissinger@allgeier-es.com anmol.gupta@nagarro.com kumar.sourav@nagarro.com noel.cunningham@nagarro.com nuwan.weerasinghe@nagarro.com neharika.gianchandani@nagarro.com chetan.arora@nagarro.com renee.cortese@nagarro.com zachary.wayman@nagarro.com atul.patankar@nagarro.com michael.herkens@nagarro.com stefan.basiuk@nagarro.com houssemeddine.ghanmi@nagarro.com servicenow.gtm@nagarro.com ankit.pathak01@nagarro.com thierry.fersing@nagarro.com eric.fischer@nagarro.com markus.gniech@nagarro.com stefan.rother@nagarro.com matthias.krefeld@nagarro.com martin.reinke@nagarro.com surabhi.varshney@nagarro.com brian.jacques@nagarro.com anirudh.sethi01@nagarro.com sandra.erkin@nagarro.com anjana.gambhir@nagarro.com abhijit.joshi@nagarro.com vlad.neste01@nagarro.com andrei.doibani@nagarro.com shubhra.kaushik@nagarro.com jatinder.singh01@nagarro.com fabian.heine@nagarro.com cristiana.bogateanu@nagarro.com ashish.sapra@nagarro.com zohrab.istalifie@nagarro.com rob.robinson@nagarro.com cristian.ionescu@nagarro.com gabriel.turcu@nagarro.com gaurav.tyagi@nagarro.com imre.csoma@nagarro.com ioana.comsa@nagarro.com henrik.sandnes@nagarro.com alina.feyh@nagarro.com mark.ross@nagarro.com nipun.malhotra@nagarro.com stacey.dobkins@nagarro.com keshav.barnwal@nagarro.com cezara.negut@nagarro.com umang.garg@nagarro.com bill.collins@nagarro.com dacil.hernandez@nagarro.com david.arbelaez@nagarro.com david.reuter@nagarro.com domenic.leo@nagarro.com dwynn.trazo@nagarro.com harrison.campbell@nagarro.com elisha.ghanem@nagarro.com rahul.goel01@nagarro.com joerg.liebe@nagarro.com egemen.zeren@nagarro.com kai.rickhoff@nagarro.com shobhit01@nagarro.com paul.lyon@nagarro.com frederik.uekermann@nagarro.com tripti.keswani@nagarro.com mark.mcdonald@nagarro.com
"""

# Split the emails and prepare them for tabular data
email_list = email_list.split()

# Create a DataFrame
df = pd.DataFrame(email_list, columns=["Email"])

# Save the DataFrame to a CSV file
file_path = "/Users/harrycampbell/Documents/Global Partnerships/python_stationwise/nagarro_emails.csv"
df.to_csv(file_path, index=False)

file_path