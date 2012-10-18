import unittest
from loganalyzer import StatCounter

TEST_LOGS = """
Oct 17, 2012 3:34:53 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=library&sort=geodist()+asc&fl=*,_dist_:geodist()&q=library&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=538 status=0 QTime=8
Oct 17, 2012 4:05:35 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=bus&sort=geodist()+asc&fl=*,_dist_:geodist()&q=bus&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=4038 status=0 QTime=5
Oct 17, 2012 4:05:37 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/get params={wt=json&ids=oxpoints:23233560} status=0 QTime=1
Oct 17, 2012 4:05:50 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/get params={wt=json&ids=oxpoints:55324138} status=0 QTime=0
Oct 17, 2012 4:48:17 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603936354520116,51.75970780116722&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=14
Oct 17, 2012 4:57:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 4:57:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=F&sort=geodist()+asc&fl=*,_dist_:geodist()&q=F&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=9 status=0 QTime=2
Oct 17, 2012 4:57:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=Fis&sort=geodist()+asc&fl=*,_dist_:geodist()&q=Fis&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=0 status=0 QTime=2
Oct 17, 2012 4:57:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=Fi&sort=geodist()+asc&fl=*,_dist_:geodist()&q=Fi&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=0 status=0 QTime=1
Oct 17, 2012 4:57:52 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=Fish&sort=geodist()+asc&fl=*,_dist_:geodist()&q=Fish&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=24 status=0 QTime=3
Oct 17, 2012 4:58:09 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 4:58:10 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 4:58:12 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 4:58:16 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 4:58:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 4:59:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 4:59:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 4:59:40 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:07 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:11 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:13 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2604127528227522,51.75966644287107&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:21 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2604863810703102,51.75966644287108&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605400010955152,51.759721725296004&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:23 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260549472646099,51.759718372534735&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:24 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260549472646099,51.759718372534735&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:25 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605738639843282,51.75970186018549&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:26 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606000155222234,51.759676379199846&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606255803268966,51.75965232313774&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:28 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260646367446762,51.75963245802723&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:29 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606677412998495,51.75962625541888&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:30 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260689366610032,51.759621561553104&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:31 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607226427656233,51.75962177110068&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:33 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607706710707962,51.759627512704355&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:33 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607490457606136,51.75962030426763&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:34 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607813999068558,51.75964192957781&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:35 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607835792016804,51.759652406956775&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:36 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607805617165386,51.75966129177414&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:37 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607700843375742,51.759669296491666&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:38 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607603613298952,51.75967549910001&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:39 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607552483689606,51.75967847467564&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:40 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607443518948376,51.75968040251337&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:41 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607446871709644,51.75968220462255&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603801582020338,51.75970072862856&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260381261889033,51.75970148647852&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607470341038525,51.759683461908025&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=16
Oct 17, 2012 5:00:43 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260743932799679,51.75968823959283&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:44 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607424240571081,51.759695909034235&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:45 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260731862859112,51.75970894289367&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:46 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607114110153734,51.759725245695336&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:46 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260381261889033,51.75970148647852&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:00:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606971617799818,51.75974150658749&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:48 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606880255055246,51.75975906667463&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:49 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607143446814835,51.75974888266228&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:50 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607393227529347,51.75974322487764&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607567571115315,51.75973534588866&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:52 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607705872517645,51.7597246170526&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:53 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607820704591095,51.75971648660652&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:00:54 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607867643248856,51.75971124791704&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607859261345684,51.75970584158949&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:56 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607832439255535,51.7596984655147&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:57 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607779633265555,51.75968979024492&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:00:58 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607803162193567,51.75968796179237&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:00 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607786331201012,51.759686187239154&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:00 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607749304888525,51.759684503594094&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:01 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607676065543036,51.75968446105887&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:02 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607621756631315,51.759682558744764&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:03 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260757616464276,51.759681648177164&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:04 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607545690013564,51.75968099265214&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:05 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607463567901223,51.75967797511402&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:06 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606978323322355,51.759670008953435&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:07 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606763746601162,51.75967009277247&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:08 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606674060237226,51.75966975749634&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:09 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260671224751921,51.75966835218643&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:10 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606730740353296,51.75966757240421&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:11 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260675050790807,51.759670536468&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:12 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606809577378717,51.759673512511185&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=16
Oct 17, 2012 5:01:13 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260689483832963,51.75967768384007&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:14 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606967729225305,51.75968354085556&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:15 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607007606477842,51.75969238924792&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:16 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260705977001124,51.75970111156924&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:17 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260714763776642,51.75973169976078&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:18 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607345450681269,51.75973241222255&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:19 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607574276637852,51.759733543779475&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:21 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607574276637852,51.759733543779475&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607734370988428,51.75973098729901&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=12
Oct 17, 2012 5:01:23 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607734370988428,51.75973098729901&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:24 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607734370988428,51.75973098729901&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:25 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607734370988428,51.75973098729901&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:26 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607734370988428,51.75973098729901&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2608002591889917,51.75972218630068&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/get params={wt=json&ids=oxpoints:58828830} status=0 QTime=0
Oct 17, 2012 5:01:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606513248693212,51.75970046541786&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:28 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607792206120312,51.75972771835677&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:29 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607792206120312,51.75972771835677&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:29 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605990325050858,51.759708450355824&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:30 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607792206120312,51.75972771835677&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:31 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2607792206120312,51.75972771835677&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606966588657915,51.75974138085894&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:33 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2606810685258922,51.759740919854266&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:01:44 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:44 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:46 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:49 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:49 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:50 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:52 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:52 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:53 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260481648019002,51.75987923385058&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:01:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:01:56 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:57 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:01:59 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=6
Oct 17, 2012 5:01:59 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:00 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:02 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605624228694867,51.75979550458977&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:02 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605633147896835,51.7597948677809&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:02:03 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:02:04 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:05 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:06 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:07 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:08 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:09 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:10 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:11 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:12 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:13 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:14 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:15 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:16 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:18 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:21 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605438014654333,51.75980063695622&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:33 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:02:34 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:35 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:37 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:37 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:38 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:39 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:40 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:41 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:43 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605027033486091,51.75977894099845&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:45 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:02:45 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:46 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:48 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:49 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:50 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:51 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:52 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:53 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:54 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:02:56 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:57 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:02:58 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:00 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:00 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:03:01 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:02 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:03:03 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:05 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:05 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:03:06 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:03:07 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:03:08 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2605923433316475,51.759770803588026&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:17 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:11:18 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:19 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:21 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:22 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:23 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:24 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:25 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:26 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:27 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:28 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:29 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:30 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:31 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2584,51.7531&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:32 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:33 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:34 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:35 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:36 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:37 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:38 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=0
Oct 17, 2012 5:11:39 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:40 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:41 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:42 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:43 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:44 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:45 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:46 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603794038307483,51.759703494656605&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=1
Oct 17, 2012 5:11:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603796655369548,51.75970288431854&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:12:11 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603789071786922,51.759704621511545&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:39:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260352964863177,51.759673294832446&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=21
Oct 17, 2012 5:39:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260352964863177,51.759673294832446&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
Oct 17, 2012 5:39:47 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603535995791744,51.7596729996664&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:39:55 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260370077621454,51.7596762268444&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=12
Oct 17, 2012 5:39:58 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.260326940083812,51.759690475011105&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=11
Oct 17, 2012 5:40:07 PM org.apache.solr.core.SolrCore execute
INFO: [places] webapp=/solr path=/select/ params={pf=*&sort=geodist()+asc&fl=*,_dist_:geodist()&q=*&sfield=location&pt=-1.2603467127215506,51.7596986644494&wt=json&spellcheck.collate=true&defType=edismax} hits=9830 status=0 QTime=10
"""


class TestCoreCounter(unittest.TestCase):

    def setUp(self):
        self.logs = TEST_LOGS
        self.stats = StatCounter()
        self.stats.process(self.logs)

    def test_parse(self):
        cores = self.stats.corecounters
        print cores
        self.assertEquals(len(cores), 1)


if __name__ == '__main__':
    unittest.main()
