import pytest
from src.practice import most_commons


@pytest.mark.parametrize(
    's,expected',
    [
        (
            'aabbbccde',
            [('b', 3), ('a', 2), ('c', 2)]
        ),
        (
            'kwuzazrxreqpypvzdsnvtumobemekfskfshopevggqgoascrunynwaxolxcygnkllnqslcqrlmlbvrarepmfkdbacawcipzpbcgnekzbrhotracywrlarfawxogygnanyhtgtvdfnaluefebhjivqagvcljghgbscvkmmtnafamqffycsgufjugqzhgstmjhwzosrnveqnwahflysxumwuvxyxrmarwzbabufxajdqybetjtucqhnavugflaofmtrkkrbsszoqcvuhydsdlfwinucgtlgeejaftfyaidcklgfgkwwgjlnbwryvoqbzzbktemvhpuudgfgxwzcmwgvcnofdebcwyhxmnxefrkdlafvfwgrzembfugqxcpukvgoixedbyqjmfywqqwnhotqdpgdailabictebdgnjfdbiqbnlrbsduwebtqaevukkyheypwdksmpztideoropeepphoniddgnrsmiqsafuyxvqerkoitpqsgswtroiwralcrupfavyyfwmyzuocaeyriavmvukqhzjzubnnrecsqbjngtczuonyktdcdvukxcdcwatlvjluumjijdfemilyarwvdytraygahbpgarwyzffyoukgmdgemmmxkajwsqtkpaarjskvuldfvlydkcoezgygjfygwzwsndfmkxzuljsnnltlpnjrtkrvdzchhmaejmiatzvmyysdiqhhyihmavkcjfuauvtwafnqyowyfsnfmxxvomarjvplrqfopknlstgnnodifdiqzvliszptdcjcffzbacszftbkeorbftaqjpfaackqqobbaccwzxwbymkwckgzkoqmwiilsgitbqbfjzwkzodaqgknmxujfrdgoiupvqmnpkruxwungbfjbcpqsxizuvbpedajxkncbcunlrkwiokezfdgkdwiiukwcktftfzzslnsojtpjwziiuyiutkhxpasblitpjlxerdvhwgtpddgqfyuyzesiccvgkwyfwohoupwmrolfklonyqzjlqeudamffigrlzaevwbccenojadkxeimomlfhqvhtayvzlmvvutnqvewqhjsqilimessmlvrrbvyvkpgahvqrexhnxptxyokzorxxiwozvmsjabeqrygljcvjfksvnsnoocnwgwuelucefyjtpdndaehggveotcbieawteoafihpxixkfvxezknxtnyzwgdwzsiiodlmokthekehtzgwtglnsajikalneolwjddizaoslvxxbrejwngjmafwprmhvqtoiekdfgputwwcmcgzbnhzrprenikdtgcsvzzkzcfgqyrvhommotehbulrnhmdgttbctmoxxwosvypmdxeqczvxrytubvdsdyybocipfmxlplhkfiejtdfrgukhqtdzressilhdxmqrortqkcuxjrnttsmsoeygboztakfpbbrxfzsdzzdluzqsdqmwspctlsacrlevxydoyvjkzorizimrdzrmzbjtrsqijsldyhpslluxtuiywkjfhhebndzkmbtkboiuzhdcwgypqjwqapzvwborqekdwqytpzcgxwxgnxemonwlescunaseuyokpwotnqcyvjjhylcaxlhpulxxijljfhflzadncbjdqwosbgicdyjbuelpjztutufujhxdnzkbwtzienxmcbxtfhifepbocycnemphavdsdylzfvziznrtfsshcnbfcsykegqokinhqblbcsrmxcwhwwjvukfyxhpeoqqotornsomdwboiymvzjunlbnivptahxcfftqmcxbxavsuicxxezjklcqbyujckxojyjxacnvdptvwuzguwhbpoajmdrrqxoiubxnjwjfqhzrcsbzdsaxzinqjhknjnjxuwlnpzbwrbrttohdmltxdqesavkhbawwuyzgzbdmrltobnyuxcvlmcmncziwbtzissojcyzfuhbbxdrahjlkjktuzsphcfmgkleschnqjdeovjqyysbgdeuvulzfsfjygezmeowwpwshrbqyfegkarkxpdztxkfcdhncaqjbbnvwzhcxmqxfdazrtiektdepseomsmqcnbiwwgtvzgxkypieeoojpazahbcgiircwydmusmudncuplrbrlsihqwomvipoexwazsdtggvwfscaippzctttuofgdipmiqicreumjscueevvuvcubiiikhzmcgndjeisraarrmjolyahddukyfowxarkmcdrwabcvcsfvsphozszbobxhzaymnwfzfwswrgqlwlstxihdajvnhvlzzdbqxuiigdgsmitsiirfiqkfcsnplwfprsbhtvukbvuukwaodwcqeaapeyixybuxijhohglzlyvoegyjovolmcxtxwukswhewucpbhaeiyqwspqiyobmtivnjawfxayibgadadygbvdcvioxnpecpnvivqxiqpeywiwgzicqzdxlaijsnhxboigwmetyknaxxhlbcznwcypeyjzyvhvemaycydcixelpkxhovqqziyvbjuyykmsxidubxvzvbycnkowbddqltpxzsdwyfivjqsnndtqokshbecnirxxwqhwthrzfadkdzlorwcwkfvmkglxhaiiexjeobyvtizjgsnzcdiwutvhotgyycurkibbkmjbeljdtldhpaysaufjacdapssronnvxkvydbehxmvmfhmudemmnfrlfvhwzdcdqywcnjucjyljjgdznrayqsfxvhfaznnnqblaqvflrrvrpujemcglqtyndqwapfytxpnrhdtumifokqeovtbyszckviprgidsvzbswhkaocjspubisoweoaxmuiynybqszarslsrfbsvbodzuetztqifpwtwvkfgtynzfcrzovnthwobbsbbhgtzteqpsglchkevhjgecwlmhaglaionpkhpfevbmrltntiesahjaafokkyxvtxkxnezyavmabjhxhxdklmjdyfejbpqudaoinfjwzbvvmjyjnyflsohuhadnthxptlnktqknwvbwsfvlrwkjkoboqqpljvsxjpxcfqfsrivbtnyjxgklbjjhzfiodlgjxcvotafmhshglrfdraxzbeqpmddslioeecfsqurfryltwzlqellpqvjizdfndcqtkuzoaagzwnkdmzixgpndrlmqbmjvmoxvmuypsxhtigvwfncashqqjfcmculsnoswegmepizuugkvbvjmiwztrdzhbzhqumeiswsdouiawftqjclzxfgjzrjrrlkknmddyjxlauppaewdlfwekpfslxweuhfuyiltsoyfgnxtdhhvyjkdqayzcmpbgrmpptawhxpsijutzhacvubjntlzmrryaesogojbikcuuuaiyombqyujwxrbggiringxommmtsawjcykdhfetggfjaihbrrfvmwzcspbdxtifgxcpcqmuodtdpwqumiyoquurcpguzjucccndqqzzlvempkvjiwtjnhveyraczjuxzfkzftnfmvydgsxfwmkgolqoinpklcjplrbxyoliciybnudvxxloqtngamrlrdxolplcwqftjovtbdnmxnksjvoosggjfvslagnzadawbanudghbpezkirtnwgueeowrbnkbdtqsoynpftpofmjdtrhpymfnnwtnhepjksoyfdtdwhydutnbsgkgigyhgtbryruktazneowripzvgpnzdxhfjcqflsdpjhabzjoxjeigguhkjfmzypduakqyajxqfygeygeyyltlyeygpkqfeolmwoocajrkcvqztnzkdpsqtcfedghhesobhxjjnhroorydhagwllqpugrxwhfxhhuqozniqunjxbngdottuawzkhkqaumqononncyzzwfqguswpjmnjnnyytbznoxsmfsnlbszraxmlljgmnhmetowcbperxjjaebvaljjjxhvqnlcfqyzzvfywhkjnvufmtaexhpwiclpwlwepzzfclfcftqcbbmzpxhksiurcjlgkyufwaxfqfqsqochugxqsgrmzghbwnbskmuiawozuodaaoihapopqxvzhxitwdtojgxmkkqbmuljafddtqohszckinrcaeghhlsvaoosbwszgrckdcfkzuynvagavdmdbjaqngfyhozkkqqlwhiitelcbvpircblhmwhrqjbsqtgxmjtmojsorlxvrhehsqkxjuqpylpngiacfmflgabkhxtiowwvjlsjmufqmsgnosddyxohrztrxbbdjhhiaucqygywihlfejnoxqtxdhxdtndixjnwaxhdefuqcfbepmmgcdenvgoeyrvtoeaydrgbiqzwequcmoyghldhgmeplmdsskrkueaamlrjklfldhushjmjjqdpharwkicfuazwamjuozvgtytzctmnkfifldetfrsxrznocrebqkuaqnrixmcvnidujcvgwgsowrpasnyzdbwpmdirjhlrsdlnavtgzcubhkjinuxphopmvtsfkazrgdfumjydhehxkdlvwtjikhidytcxpppnthckdjecqfroujholphmjsupxfdcrhjnyrcblqjoqftkbgdrjbijzlqpvzwmglqvtaxucfzucfmjiaqnujxbojcahgouewwiddbblzebzrwjxmdtbkgdfywwxwnymaxlpurujvabouoqgzgbjujpqrghragulhvdcjvlpctvcaytmjznewglyipuwlupfswzbwmommlrrbzrlmuyhgvpfqrdrzkzeykfmywaehsdqflljvvpwkxpksqjkdcwroukoselfugujtstrllayabeumkyxgvlglkyeyqxtdfwgvdbuhnwvcmuznwcpocrqptjhrspmdeygbvuropxcpiimtlliyyfhzabhycohvwimdvpxkhhktyfshzwfvjmbwqmgnasfqcjtgzhuufxrreqxrvcwzfojohdlwnbwcwzckcekwmwmfgcuyhfamigyndjllfbhyesnaceglwlojgywrfobvxswmhkvjqeargkkrcmyklxfcgmdutitedwkubaaasnywflzvzuqjuubyrdrbletdwvwlivjfiqiedisurfnowcruvygmmayamwucbjafhsvejhfmmtellyxwsqowrgiapxdhxrkxtqcwmusttwblhutfrungizwalkukfctpvfbzlqmryxblsawclrjggyuatagymrvkzildltdbbcfyuehonedcnbuwlklcoqvmqmkxzjagmjjrgdquhvmgsyetgtohtuqqjmimyuzpcxxynmaafycqijpqndqzxhpokrvhfgqkxbjbhksuahjgvrqzmihwsqoijjkyqiyrmaybxpxcyacwmkcypkctfuyrriluytxvprrltvzsvxahrrxvjfvevibxibobssgeshmuuecdriiriduzuetdkynykacqlyzilpmfllfdgyhliwozeufydbklywrsfokxgdbhopukrguijughxkxogfolmcaudxcxeescfgabcaxumduflrhveicgkfdaophlalrtaxkxdriofndwwttyeunmochhibtuhpfnaxtmmtsumqsbnuhoknvvrfqolsaksaqfpxdombibnfsvyuhifayekztvoffcdzsyazflmfjbixbvmepwmudyahzhcpqyyzuyzcwosnznfuwfcblbtpgtzsunwyofdrzmofymxurdwzjuniqxthiavxschkgcxefaefqyjlvrzsvyxazxfgldlbxviylcwgebvkgblstpxzyotmfjdaysguvbxshkfijujvuxbzsdhwwsacrgjaufqyfdiaanllsnicwzkxijpvhwbdmlazituxlbucrmhzyksnwxcyatrcopmxcfcgqjpvglqayqwepegahyycrwpbbwaukazemkrsuloavslvkatjjqyfcwxgpikeyonxyqsiwuoahrghpcwwmvybgaonncehqqowyrumcwywlzttkogzguzcezqkcddazstseyhhqyjkebeuyyemmivhmykdkuruydrdgrhfcwwqjmefsrbuygbifvuktcccaafvniqdzmtrexmxcxzezqpkhtqpqjgdlvtcdgwfaelhitiahscbsqayziexemqiiijzchleekfdalwqcijlupldqamwozuatkjwbyvhwwrfvrqsirkizhfkizvtjtyixbrypodrhobkafwllypbrwchbpfuyufxtbjfapixaeaqxnepnpwybhqdhyygprowvnqwrjcnphbuqfxstwuxvywuemagwtujlacjgtriyluxcexjyttvhmrjkmpqohxnfxwmlktxgpakmgsvqxkjblqojbneovlzjqoxcefiwrqpeifgoxdhojzxszhdwfiggknbgdhlbezqglnistwuznojwvawnddwuwgwiejxmkuaepmcsbstygejuzojtdtqmijfvhfxydxxloowtyirjomtjpoobzxxhjskwjnvqofwzscnaxqhfouzimwywvimjwetnycttihkavywijbxfhfaihkkmyaxudbwdboalexekqyoysjuftwrsgfylazwqaigydkpwurnoekklcslzrslfcimosbgxoxzdeosdpvizornqygmfyteebjwpcxrwfudjiffymgiahrmfgvinntgtnbwhyhzjnsjvwwshzqnpnknjitienafvnwulzazpaoeubcsntohchmiqeunrdzyubelmxfnfsppcaqktboibpnqhzjktivwcfxvajjbgdyeabcqqwkfrtmbztayxhaclopmhccfaazkhrgixumhiglcjnucdyamzwykcqrvtlzxyemavvijaeztdqyuykavjdoawrztqfmibjhhetagnocbyoyplkmlwcwqezbgyhluhnwzvxflookbmlzyecstdwbubxkpnfhhimbkjzjvmcroaicbvvylbvihkoynpcntcxlnifyngaqfcsiqilcxjnnmibzfpwvjggzaysniuovokrllnuzlacjownthcxcfeypmttairpjfvhlyycidoymqfqhdvuxjedhfnziekdupaqqtnaaskssynplfthzxrklhmlaiqiposkvdzebevhufrskddkgxebikqcgbqmniwmiezbxwabvmcxgjifjfodswhfkdgtztvfwswlaghntjjdjwhqqjiowmvoomjkvximghjkzwksmaslucaaosodaipjoyuzunbqvklmkaemtjgezmakixjremydttiqbxgjklhpnrlpyghsvmymjuagtnjwbpqekwsjumjjrlchteyezhwurzzxneeljvagpmsbsmzrsvonnwprsvvxlqdqtwsrvrujctcbeidprubrjblaknjgpkmjeydsmzladtpvrjvegooirfaxpkogittojawoiqyldlyukdotlvthdmsewsrumnuzfkdqfquytwvhubjsfkfgoytjnzcpcwibhipphlblribtnqgtrzfdrrylyqiylkcmdszekzbwevzhhrslelbzjitdhngpxwakdvnzflugsdiopuejcjzpwmcdfiirvgthbcmbdvbveupybtmleywkosugjedkscqozicdbchdcwzrtexryzoxtvifihjlqsjxlhidgmvcwpvwgcqwdoeyqcsrtqzcrpkhdkjolouqcfaxhemygintpexlhpknhkvvaqveimhoybjjhzhmlpnvlckjbbcvsllzepjlytlwxdiwfpxkbhjabxoeeaoiigklvchwkpojhwgpslgnpmdomgvibndvyawlegmluyslswkdmjynwzjpxskbjjxntgxiblzrdqpkoujhgthmyulewzlcyodzdmoucjjbhfxuvrwktjkvedadpdeejuzdukiucklpfkwgjscndzefkjhzarezihprhhwqbsblljacukxkysyaqrogiozyycdodtfqiyvogvxdfdespjmvcysgoocqkuipvpdtpuhvynefiygtbycuknbpmrupnhhgoqsecivvpdcnagnzikjdladycquofusbystphrmsmqsbxodnidrcowolovftzzrhsienmnlqqfmxynknahogluxeubfspfvbygugigexaxqfnvvzitgcsuhrwyhtdezndoafsztredvgwxkngxgitudnmspkwougjkzkcrfkykzajrjudrllwmbqucvnkvrzayvqubrcqjqckbvuvndfndefbluizhaeexgvazbcybnsezekktmannynrnnruumswoacezjojedbyfhetnnderbsnjienxlvboksebbdqxmpkgqmfjfxbgcwsqfjjgfkffvaermerksrpaukjznyjcvixzhfydcoxleojespijcplugwghfpfovvcbebqdwxtdllcvkhseeodqunrcgrfhjmwdgahnxzsdsntpzdyoilcgdhtexyjylutcwwwfsnbttotxanoujtjrahsghuabchxgwxcgygjckaaipniumdoxitzollqsydxwvknmnntcoixapnvoibtimigntnkhscbliqrxmecwealszhgueiilhvkjfhojnqxqjvqfuslueuvnpretcpoarugqcbwxjrsuphwrpqfiyifqqglnodsklqkzfgbhuegkhydvgmqzpacnszappfrrgjvbmbofqasttolrayyqzcrtttrdlrevaigzacxnxqcnbfwadzemqtrzbfqspxzhixuopzgbadstyzvsvvdzrezflzqsztpbntyvwjxqmsjyxvysgljcljlssmkvvfdddnuaprvwckmsytuswgpyzdwugiaaazdswqnwwkjilmcuoaxwbxkjzzrgyktnnlxmotwscstbnatqwjxniwmmxuwcacnyqhxlebmaxyzgyimdleiizzzoemmgzqkldpjwapssincomsdmrnrdvfkasxowcnqiglwbhnsoafmilnraahhdinytvxifywnzkeijjyyrqszlyayroptawbtfltrwiptatybcpleliogjvakiimxiyaslcbrctauayvknjvmrwfnsygntfcjngmxjjewlgtpsnnnykxrlcsbwakctlcbjriamryryeoogsljfbifuwperegwhwzmioeenhumyaspgwkmamfiryvxrphhoyhtgysjpwrgluetawshwkdxwtotbswhnamtpjxpshfcidynfgujjdrfvsbfjtnbbhiguxztqrncnolvfpeugybdvmorcshvtktlryqcturaejkplklxagqcerdtskibgyzkqeeiegjqhbrhtuzxhgqfbrmvdvxysirslythfwvivsdlpswsicjfqmkatjmpbguvippmctkbfqydahrsjibvwtxlnviwtycrjyhttsadbrisliftdsfuxgtmepayfvvbojovkchjwvhkvxlwqbqfwbmdfgkpjlhpezktyldimbopulmophlojjuowcqcazdecplmwgouduzdsebmaywbwuyhghmihxnluzrljghanrutfrwsdsefvswhectmhvfanovgyzjatxxprfejxgzssqnzpwaamgqiatahweshqjhehkefakrksxtvplzmoxwqdpyydjpbpbitvtlhcfpvqmwvbunurzydqrvuhhhmxbpxlqarrakkaowyhtxqyvpewbalneiszceegrwraludumqlqgfdamyemjoyvvugwtarrowjppbpuepptvmmrmllaldtkesnonaaewdevlbnvczvlvnjmemxxsfdwdusvooqzamgjkqlpfdcatvjmaaupehrjbzhauqlyhkdkomltcrcxllagcbzjvtvrgqzodghxygtlinkbjlyhszvsrytgbmavvayfocokugpazjzjgnkaflunhztnswjpagjbkjlflydagnzsfhuuficmttrogefyxtqpkrptnlctquhyhpeuhtqguxmv',
            [('a', 419), ('w', 416), ('y', 415)]
        ),
        (
            'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni',
            [('o', 12), ('m', 11), ('n', 11)]
        ),
    ]
)
def test_most_commons(s, expected):
    assert most_commons(s) == expected