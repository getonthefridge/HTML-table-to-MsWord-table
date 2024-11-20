import subprocess

from bs4 import BeautifulSoup


def getCaption(soup):
    captionList = [header.get_text(" ", strip=True) for header in soup.select("caption")]
    if captionList:
        caption = captionList[0]
        # print(caption)
        return caption
    else:
        return None


def main(input_html):
    soup = BeautifulSoup(input_html, "html.parser")
    columnNames = [header.get_text(strip=True) for header in soup.select("thead th")]
    output = ""

    caption = getCaption(soup)
    if caption:
        output += 'merge this row ~ |'
        i = 2
        while i < len(columnNames):
            output += '|'
            i += 1
        output += f'{caption}\n'

    htmlTable = []
    for row in soup.select("tbody tr"):
        row_data = [cell.get_text(strip=True) for cell in row.find_all("td")]
        if row_data:
            htmlTable.append(row_data)

    for i, col in enumerate(columnNames):
        if i < len(columnNames) - 1:  # Not the last column
            output += f'{col}|'
        else:
            output += f'{col}'  # don't put a | at the end
    output += '\n'

    # Handle rows
    for row in htmlTable:
        for j, cell in enumerate(row):
            if j < len(row) - 1:  # Not the last cell
                output += f'{cell}|'
            else:
                output += f'{cell}'  # don't put a | at the end
        output += '\n'

    # Write output to clipboard
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

    if caption:
        print(output)
        print(f"\n\n'{caption}' has been copied to the clipboard.")
    else:
        print(output)
        print('\n\nThe table has been copied to the clipboard.')


test_one = """
<table data-width="650" class="frameall" style="width: 867px;"> <colgroup><col width="200"><col width="333"><col width="333"></colgroup> <thead><tr id="MVLX8DSDSUVLA9TL0114" id-sequence="344"> <th scope="col" id="PMYKYJ06A2YDDNC5Y226" class="alignleft valigntop underscore sidescore" id-sequence="345"> <p id="DQEQTS1AF3F4AV4YA601" id-sequence="346">Asset</p> </th> <th scope="col" id="CBGAD9KB1LZG2L8XN563" colspan="2" class="alignleft valigntop underscore sidescore" id-sequence="347"> <p id="EZQR0S7UMH66ZBRTM831" id-sequence="348">Description</p> </th> </tr></thead><tbody id="XKSBQSEX5BXXWMV99606" id-sequence="349"><tr class="odd" id="QHLUZ9WNPB87J4H6K006" id-sequence="350"> <td id="XYGRL8E4S3ZNJ8NQ8877" class="alignleft valigntop sidescore underscore" id-sequence="351"> <p id="EFQKJBGQZ39QN3FXB280" id-sequence="352">Network</p> </td> <td id="RJNC2KMTCHB0VDR10743" colspan="2" class="alignleft valigntop sidescore underscore" id-sequence="353"> <p id="RWXNAWE9DVLA48BUS646" id-sequence="354">Can identify possible network security attacks and vulnerable systems on wired networks</p> </td> </tr><tr class="even" id="HBXZ5MMUZMZX4QHL8156" id-sequence="355"> <td id="TNNSNGNTBNPFQ3UE0723" class="alignleft valigntop sidescore underscore" id-sequence="356"> <p id="CXVWXTTHPYE9GHMXQ238" id-sequence="357">Endpoint</p> </td> <td id="FFYW66BF3EFJX1XAZ907" colspan="2" class="alignleft valigntop sidescore underscore" id-sequence="358"> <p id="WJWLW1P2BHSQCVXUH768" id-sequence="359">Can locate and identify vulnerabilities in servers, workstations, or other network endpoints and provide visibility into the configuration settings and patch history of the endpoints</p> </td> </tr><tr class="odd" id="SXFGPS73LWRKSVQ4Y059" id-sequence="360"> <td id="EYBWE9WTYBKALCKR2658" class="alignleft valigntop sidescore underscore" id-sequence="361"> <p id="KGHCPMJYKZCNGU63L982" id-sequence="362">Wireless network</p> </td> <td id="LYRVUQG69FPKHYJVQ301" colspan="2" class="alignleft valigntop sidescore underscore" id-sequence="363"> <p id="UTSYJ0C2XG9L6A08A616" id-sequence="364">Can identify rogue access points and validate that the wireless network is secure</p> </td> </tr><tr class="even" id="NTXRLQGDC68BA438J145" id-sequence="365"> <td id="TZZQK5EZKA98M5Y6U307" class="alignleft valigntop sidescore underscore" id-sequence="366"> <p id="WTCHLQFW24KWHGKHV404" id-sequence="367">Database</p> </td> <td id="WDTQBLLEFJ3D24AGD474" colspan="2" class="alignleft valigntop sidescore underscore" id-sequence="368"> <p id="LDMJS7YJ9LU1VX8R8499" id-sequence="369">May identify the weak points in a database</p> </td> </tr><tr class="odd" id="YBLTY9NPZ9N380160541" id-sequence="370"> <td id="RNQV5JXQ5WQBDUHHV666" class="alignleft valigntop sidescore underscore" id-sequence="371"> <p id="JWRQR3W0L8F4CTL1Z340" id-sequence="372">Applications</p> </td> <td id="ERHQ0NRM9MYN6Z8JQ447" colspan="2" class="alignleft valigntop sidescore underscore" id-sequence="373"> <p id="JCVEV2VFXE1EG38BB353" id-sequence="374">Web applications and other software assets can be scanned in order to detect known software vulnerabilities and erroneous configurations</p> </td> </tr></tbody> </table>
"""
test_two = """
<table data-width="700" class="frameall" style="width: 933px;"> <colgroup><col width="200"><col width="333"><col width="400"></colgroup> <thead><tr id="KHVSDJYK4Z4RCXAQ2954" id-sequence="538"> <th scope="col" id="UABUF8RA1CPEF1B20695" class="alignleft valigntop underscore sidescore" id-sequence="539"> <p id="UWYEKWAPF8J0YWJMU617" id-sequence="540">Audience</p> </th> <th scope="col" id="HEMZTYS47CFA3Y8UX079" class="alignleft valigntop underscore sidescore" id-sequence="541"> <p id="XMURGCDVBJNMW3DCJ544" id-sequence="542">Level of report</p> </th> <th scope="col" id="JCYBW0BQSRHE9TGZF664" class="alignleft valigntop underscore sidescore" id-sequence="543"> <p id="VKQG38AKUZ8N9TWT9861" id-sequence="544">Explanation</p> </th> </tr></thead><tbody id="WBKBGJA69L4DLH4FU557" id-sequence="545"><tr class="odd" id="VKRKJWXQ2N941P3DL154" id-sequence="546"> <td id="XTACU0KSSEA8W194W098" class="alignleft valigntop sidescore underscore" id-sequence="547"> <p id="JFYWG9C92MJMM2DFY547" id-sequence="548">Management</p> </td> <td id="LSEAJ9PAT3AVEZZ26618" class="alignleft valigntop sidescore underscore" id-sequence="549"> <p id="VMLFPS11H5YEWZCSH059" id-sequence="550">A general report that outlines the impact to the organization</p> </td> <td id="KUNBES2FWDN8N5LK3797" class="alignleft valigntop sidescore underscore" id-sequence="551"> <p id="VPMFSRJFG3TAJDXZX907" id-sequence="552">Management will be interested in how the latest scan compares with previous scans, how serious are the vulnerabilities, and how long it will take to address these latest vulnerabilities.</p> </td> </tr><tr class="even" id="ERHTR9BFVTE1HXUP4298" id-sequence="553"> <td id="DLCPD1Z3B83HERZFB742" class="alignleft valigntop sidescore underscore" id-sequence="554"> <p id="EPMTB3BHU4FWB0AJ0997" id-sequence="555">System and network engineers</p> </td> <td id="ZPNHMEKZN6TXS3R70700" class="alignleft valigntop sidescore underscore" id-sequence="556"> <p id="PQRYY804Y2E98ZKL1556" id-sequence="557">A technical report that outlines what needs to be addressed</p> </td> <td id="HDTXPDRN309J12LU1942" class="alignleft valigntop sidescore underscore" id-sequence="558"> <p id="SXGXM5M9252CW9TGT714" id-sequence="559">Engineers will want a listing of the devices with vulnerabilities and specific details regarding how to fix the problems.</p> </td> </tr><tr class="odd" id="LVJLZZM41RDAYTLXF495" id-sequence="560"> <td id="HKADC8BGUDTM6NUTK122" class="alignleft valigntop sidescore underscore" id-sequence="561"> <p id="PGFV934EYWR7TL6ZR864" id-sequence="562">Application developers</p> </td> <td id="JDBJZ8CRN5A2GQBBL216" class="alignleft valigntop sidescore underscore" id-sequence="563"> <p id="WBMUR5CYSWQRUSSJS542" id-sequence="564">A report that lists the applications that contain vulnerabilities and what those vulnerabilities are</p> </td> <td id="TAZPN28M2LJW7TP0N142" class="alignleft valigntop sidescore underscore" id-sequence="565"> <p id="TGLSJ41QLFA7GTRY0680" id-sequence="566">Developers will want to know which of their applications are vulnerable and as much as possible the location of that vulnerability in their code.</p> </td> </tr><tr class="even" id="VDJDY4MYW934TDB9L176" id-sequence="567"> <td id="BGDZ8F5VS2ZT89JMH425" class="alignleft valigntop sidescore underscore" id-sequence="568"> <p id="FRXGH48Y8R5FRWR6Y593" id-sequence="569">Security teams</p> </td> <td id="LKRF9P2V1Y3TT8KR5373" class="alignleft valigntop sidescore underscore" id-sequence="570"> <p id="KDRHAQZCEYU9P5N43513" id-sequence="571">A very specific report as it relates to the technical security details</p> </td> <td id="TYAWYM259VZBLRJUX142" class="alignleft valigntop sidescore underscore" id-sequence="572"> <p id="PDXFD79SZTFQ2C8BN641" id-sequence="573">Security teams want to know what systems were vulnerable, the details as to why they could be exploited, and what remediation steps are necessary.</p> </td> </tr></tbody> </table>
"""
test_three = """
<table data-width="690" class="frameall" style="width: 920px;"><caption>Table blah blah blah</caption> <colgroup><col width="133"><col width="120"><col width="267"><col width="400"></colgroup> <thead><tr id="PQGHLAWBGTXCK2Y6D999" id-sequence="750"> <th scope="col" id="EUKKZMKNQ7SPQJSV4923" class="alignleft valigntop underscore sidescore" id-sequence="751"> <p id="UCDQ0BECA7M3JM63N171" id-sequence="752">Team name</p> </th> <th scope="col" id="VTMLS9WZZ6X2YUZ5Z141" class="alignleft valigntop underscore sidescore" id-sequence="753"> <p id="BLBLZNYY9XS06QQJY397" id-sequence="754">Role</p> </th> <th scope="col" id="WXQLDCVMADPSN7K7J146" class="alignleft valigntop underscore sidescore" id-sequence="755"> <p id="DANF8QZN8P5M9QEU9167" id-sequence="756">Duties</p> </th> <th scope="col" id="EADMZ8WPJMHNMM1QQ357" class="alignleft valigntop underscore sidescore" id-sequence="757"> <p id="PFGJN7X616F9DASXZ776" id-sequence="758">Explanation</p> </th> </tr></thead><tbody id="BQTPWZW94NGCQAHKF811" id-sequence="759"><tr class="odd" id="BEVRHK4F7L79Z7X14456" id-sequence="760"> <td id="XQFUSNUJW09PCCM7K173" class="alignleft valigntop sidescore underscore" id-sequence="761"> <p id="SFXTG8A6GCEQS7681582" id-sequence="762"><strong>Red Team</strong></p> </td> <td id="EWMN6QCFFXCYBMR7U631" class="alignleft valigntop sidescore underscore" id-sequence="763"> <p id="NFTXQPEBT56V1JNXS103" id-sequence="764">Attackers</p> </td> <td id="EQDY7DGMRXHM0STQB581" class="alignleft valigntop sidescore underscore" id-sequence="765"> <p id="ZFAYZX4Z52DVVBBBF775" id-sequence="766">Scans for vulnerabilities and then exploits them</p> </td> <td id="SXGW7H4RJ7WC2UKNQ846" class="alignleft valigntop sidescore underscore" id-sequence="767"> <p id="PVMV4RTYVAFY4G0FM121" id-sequence="768">Has prior and in-depth knowledge of existing security, which may provide an unfair advantage</p> </td> </tr><tr class="even" id="CAFHQ0NCL3QU85C9Z572" id-sequence="769"> <td id="QUGC88LZ0RM4NTJMY818" class="alignleft valigntop sidescore underscore" id-sequence="770"> <p id="NHFFTL16D0LQXH8QK977" id-sequence="771"><strong>Blue Team</strong></p> </td> <td id="ZPAFB0U38AH139GZZ537" class="alignleft valigntop sidescore underscore" id-sequence="772"> <p id="HSGY9BZW0VZ5NCNH1984" id-sequence="773">Defenders</p> </td> <td id="VEHPDMJ1V77861GLT416" class="alignleft valigntop sidescore underscore" id-sequence="774"> <p id="JCUWPQRXQRV9L6JL8947" id-sequence="775">Monitors for Red Team attacks and shores up defenses as necessary</p> </td> <td id="ZPVTM0CA2U3KA5RPE747" class="alignleft valigntop sidescore underscore" id-sequence="776"> <p id="FHVYLFXJ0WYWTKN8G360" id-sequence="777">Scans log files, traffic analysis, and other data to look for signs of an attack</p> </td> </tr><tr class="odd" id="AGYYXD79E751TLTDP924" id-sequence="778"> <td id="SUTQB3XPT8TYTFD9J759" class="alignleft valigntop sidescore underscore" id-sequence="779"> <p id="THHX0DS8KZ5KQDQLX531" id-sequence="780"><strong>White Team</strong></p> </td> <td id="CMSZZLUV7DDT34AFX317" class="alignleft valigntop sidescore underscore" id-sequence="781"> <p id="ETUXFNZAFQ7FB01RB661" id-sequence="782">Referees</p> </td> <td id="PTBM95UKSF45P0452403" class="alignleft valigntop sidescore underscore" id-sequence="783"> <p id="BGYZXFPKT4WCS3AEK272" id-sequence="784">Enforces the rules of the penetration testing</p> </td> <td id="ZXDKQJYCU6Y00R6NN157" class="alignleft valigntop sidescore underscore" id-sequence="785"> <p id="YPAZMAKW84DST5M74135" id-sequence="786">Makes notes of the Blue Team’s responses and the Red Team’s attacks</p> </td> </tr><tr class="even" id="DGJQYTKK43UZP40SV558" id-sequence="787"> <td id="HTRZVRB0HLQBUZF14088" class="alignleft valigntop sidescore underscore" id-sequence="788"> <p id="GMVCR5MG25N0MJCMJ121" id-sequence="789"><strong>Purple Team</strong></p> </td> <td id="HLPF6PPXX77FMVBX8954" class="alignleft valigntop sidescore underscore" id-sequence="790"> <p id="VFXC7XCCM85452KPS132" id-sequence="791">Bridge</p> </td> <td id="QPJGLCBWBW36KFE22309" class="alignleft valigntop sidescore underscore" id-sequence="792"> <p id="LJBX0U1ULASUZXWFK399" id-sequence="793">Provides real-time feedback between the Red and Blue Teams to enhance the testing</p> </td> <td id="GDTBM88J968EFUNUW875" class="alignleft valigntop sidescore underscore" id-sequence="794"> <p id="NQAVCCH4TZ8BSYYSY742" id-sequence="795">The Blue Team receives information that can be used to prioritize and improve their ability to detect attacks while the Red Team learns more about technologies and mechanisms used in the defense</p> </td> </tr></tbody> </table>
"""
real_test = """
<table class="uc-table table-bordered sorttable table10"><caption>Table 26.1: The <code>jobs</code> command parameters</caption><thead><tr><th style="font-size: 17px; line-height: 140%;">Parameter</th><th style="font-size: 17px; line-height: 140%;">Description</th></tr></thead><tbody><tr><td style="font-size: 17px; line-height: 140%;"><code>-l</code></td><td style="font-size: 17px; line-height: 140%;">Lists the PID of the process along with the job number</td></tr><tr><td style="font-size: 17px; line-height: 140%;"><code>-n</code></td><td style="font-size: 17px; line-height: 140%;">Lists only jobs that have changed their status since the last notification from the shell</td></tr><tr><td style="font-size: 17px; line-height: 140%;"><code>-p</code></td><td style="font-size: 17px; line-height: 140%;">Lists only the PIDs of the jobs</td></tr><tr><td style="font-size: 17px; line-height: 140%;"><code>-r</code></td><td style="font-size: 17px; line-height: 140%;">Lists only running jobs</td></tr><tr><td style="font-size: 17px; line-height: 140%;"><code>-s</code></td><td style="font-size: 17px; line-height: 140%;">Lists only stopped jobs</td></tr></tbody></table>
"""
# main(test_one)
# main(test_two)
main(test_three)
# main(real_test)

# main(input("Paste the entire <table> code below:\n"))

