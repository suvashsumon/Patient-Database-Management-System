import sqlite3

from fpdf import FPDF

from userdataclass import jsondata


class MakePdf:
    def __init__(self, id):
        datapath = jsondata()
        database = datapath.getdatapath() + "/database.db"
        conn = sqlite3.connect(database)
        sql = "SELECT * FROM entry WHERE id=" + str(id)
        cur = conn.cursor()
        self.id = id
        self.name = ''
        for row in cur.execute(sql):
            self.name = row[2]
            if row[3] == "male" or row[3] == "Male":
                self.sex = "Male"
            elif row[3] == "female" or row[3] == "Female":
                self.sex = "Female"
            else:
                self.sex = "Others"
            self.age = row[4]
            self.address = row[5]
            self.cc = row[6]
            self.oe = row[7]
            self.rf = row[8]
            self.pathreport = row[9]
            self.rediology = row[10].split(',')
            self.mri = row[11].split(',')
            self.xray = row[12].split(',')
            self.ctscan = row[13].split(',')
            self.pics = row[14].split(',')
            self.dxs = row[15]
            self.comments = row[16]
        conn.commit()
        conn.close()

    def printwork(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(auto=True, margin=10)
        pdf.add_page()
        pdf.set_image_filter("DCTDecode")

        # heading -> Personal Information
        pdf.set_font("times", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="Personal Information", border=1, ln=1, align="L", fill=1)

        # content -> personal Information
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", 'B', size=11)
        pdf.cell(30, 6, txt="ID:", ln=0, align="L")
        pdf.set_font("Helvetica", '', size=11)
        pdf.cell(50, 6, txt=str(self.id), ln=0, align='L')
        pdf.set_font("Helvetica", 'B', size=11)
        pdf.cell(30, 6, txt="Name:", ln=0, align="L")
        pdf.set_font("Helvetica", '', size=11)
        pdf.cell(50, 6, txt=self.name, ln=1, align='L')
        pdf.set_font("Helvetica", 'B', size=11)
        pdf.cell(30, 5, txt="Gender:", ln=0, align="L")
        pdf.set_font("Helvetica", '', size=11)
        pdf.cell(50, 5, txt=self.sex, ln=0, align='L')
        pdf.set_font("Helvetica", 'B', size=11)
        pdf.cell(30, 5, txt="Age:", ln=0, align="L")
        pdf.set_font("Helvetica", '', size=11)
        pdf.cell(50, 5, txt=self.age, ln=1, align='L')
        pdf.set_font("Helvetica", 'B', size=11)
        pdf.cell(30, 5, txt="Address:", ln=0, align="L")
        pdf.set_font("Helvetica", '', size=11)
        pdf.cell(50, 5, txt=self.address, ln=1, align='L')
        pdf.cell(190, 2, "", ln=1)

        # Heading -> C/C
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="C/C", border=1, ln=1, align="L", fill=1)

        # content -> c/c
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5,txt=self.cc,ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        # Heading -> OE
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="O.E.", border=1, ln=1, align="L", fill=1)

        # content -> OE
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5, txt=self.oe, ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        # Heading -> rf
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="R.F.", border=1, ln=1, align="L", fill=1)

        # content -> rf
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5,txt=self.rf, ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        # Heading -> path report
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="Pathology Reoprt", border=1, ln=1, align="L", fill=1)

        # content -> path report
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5, txt=self.pathreport, ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        # Heading -> Dxs
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="Dxs", border=1, ln=1, align="L", fill=1)

        # content -> Dxs
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5, txt=self.dxs, ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        # Heading -> comment
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_line_width(1)
        pdf.cell(190, 5, txt="Comment", border=1, ln=1, align="L", fill=1)

        # content -> comment
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", '', size=11)
        pdf.multi_cell(190, 5, txt=self.comments, ln=0, align="L")
        pdf.cell(190, 2, "", ln=1)

        pdf.output("/home/suvashkumar/Desktop/simple_demo.pdf")



if __name__ == "__main__":
    obj = MakePdf(2113)
    obj.printwork()
