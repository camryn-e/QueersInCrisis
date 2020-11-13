import pandas as pd
import csv

## If you want to render an actual CSV
csv_file = 'crisis.csv'

## Edit sharing positions to anyone can view for access without OAuth
## Give the SheetID for the spreadsheet
googleSheetID = '1z5nVHhYdW_GGspZUPWNtXzZsz5_YIvS3eh3SaexlO0s'
## Choose a specific sheet from the spreadsheet
## This is the number after the edit#gid=
worksheetName = '300334505'

class Organization:
    """
    This class cleans up the information found in a physical CSV file
    """
    def __init__(self, name, contact, email, phone, address, website, state,
                 crisis, counseling, peer, health, addiction, homelessness,
                 advocacy, medication, other, notes, etc):
        self.name = name
        self.contact = contact
        self.email = email
        self.phone = phone
        self.address = address
        self.website = website
        self.state = state
        self.crisis = crisis
        self.counseling = counseling
        self.peer = peer
        self.health = health
        self.addiction = addiction
        self.homelessness = homelessness
        self.advocacy = advocacy
        self.medication = medication
        self.other = other
        self.notes = notes
        self.etc = etc

    def to_dict(self):
        return {
            'name': self.name,
            'contact': self.contact,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'website': self.website,
            'state': self.state,
            'crisis': self.crisis,
            'counseling': self.counseling,
            'peer': self.peer,
            'health': self.health,
            'addiction': self.addiction,
            'homelessness': self.homelessness,
            'advocacy': self.advocacy,
            'medication': self.medication,
            'other': self.other,
            'notes': self.notes,
            'etc': self.etc,
            }

def csv_approach(csv_file):
    orglist=[]
    with open(csv_file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r in reader:
            orglist.append(Organization(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r))

    df = pd.DataFrame.from_records([s.to_dict() for s in orglist])
    return df

def read_from_sheets(googleSheetID, worksheetName):
    """
    This function is based on the code at:
    https://kanoki.org/2018/12/25/read-google-spreadsheet-data-into-pandas-dataframe/

    It uses pandas to read a CSV from a public Google Sheet.

    Parameters
    ----------
    googleSheetID : str
        The specific ID of the Google Sheet link.
    worksheetName : str
        The GID for the specific sheet of the Google Sheet.

    Returns
    -------
    df
        A pandas dataframe.
    """

    ## Export the Sheet as a CSV for Reading
    URL = 'https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid{1}'.format(
        googleSheetID,
        worksheetName
    )

    ## Read in the Google Sheet
    df = pd.read_csv(URL)
    return df

def setup_HTML():
    """
    Based on: https://stackoverflow.com/questions/50807744/apply-css-class-to-pandas-dataframe-using-to-html
    Set up the minimum HTML required for a JS DataTable in an iFrame,
    including jQuery. Add the Font Awesome CDN and oSTEM Favicon source.
    With Python, you need to double the braces for the correct rendering of
    javascript functions and CSS.

    {fa_key} : The font-awesome key (if there is one)
    {table} : the output of to_html
    """

    html_string = '''
    <html lang="en-us">
     <link rel="shortcut icon" href='https://clubrunner.blob.core.windows.net/00000305556/Favicon/favicon.ico?time=637407227082223373' />
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
      <link href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css" rel="stylesheet" type="text/css">
      <script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){{
                $('.dataframe').DataTable( {{
                    paging: true,
                    stateSave: true,
                    searching: true
                }});
             }});
        </script>
    <style>
    title.hidden {{
      visibility: hidden;
    }}
    html {{
      font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    }}
    </style>
    <!-- Hidden Title -->
    <title class="hidden">Crisis Resource Table</title>
      <body>
      <p> {fa_key} </p>
        {table}
      </body>
    </html>
    '''
    return html_string

def update_colnames(df):
    """
    Replace the Spreadsheet column names with shorter names based on their
    known order.
    """

    ## Get list of column names
    current_col_names = df.columns.tolist()

    ## Decide new column names
    new_col_names = ['name','contact', 'email', 'phone', 'address', 'website',\
     'state', 'crisis', 'counseling', 'peer', 'health', 'addiction', \
     'homelessness','advocacy', 'medication', 'other', 'notes', 'etc']

    ## Rename the columns
    df = df.rename(columns=dict(zip(current_col_names, new_col_names)))

    return df

def write_html(filename, html_string, df, fa_key=""):
    """
    Save the dataframe as an HTML table with customized style. In this case,
    "display" is a data.tables default with striped rows.
    You don't need table_id, but it might be helpful for other iFrame approaches.
    """

    with open(filename, 'w') as f:
        f.write(html_string.format(table=df.to_html(index=False, \
         classes='display', escape=False, table_id="CRtable", na_rep=''),
         fa_key=fa_key))
        f.close()


def awesomeify(df):
    """
    Add in font awesome capability if you so choose.
    The following symbols were chosen to stand for certain things

    """

    ## Deal with categories
    form_categories = [
     'Accessible physical location [wheelchair and mobility aid accessible]', \
     'Age specific limitations', 'Firm costs', 'Free', 'LGBTQ Competent', \
     'Member only', 'No insurance required', 'Other', 'Remote/Online access', \
     'Sliding Scale'
     ]

    ## Key of categories replaced with Font Awesome
    fa_key = '''
    <ul>
      <li>Accessible physical location [wheelchair and mobility aid accessible]: <i class="fab fa-accessible-icon"></i> </li>
      <li>Age specific limitations: <i class="fas fa-child"></i></li>
      <li>Firm costs: <i class="fas fa-comment-dollar"></i></li>
      <li>Free: <i class="fas fa-money-bill-wave"></i></li>
      <li>LGBTQ Competent: <i class="fas fa-rainbow"></i></li>
      <li>Member only: <i class="fas fa-lock"></i></li>
      <li>No insurance required: <i class="fas fa-notes-medical"></i></li>
      <li>Other: <i class="far fa-plus-square"></i></li>
      <li>Remote/Online access: <i class="fas fa-globe"></i></li>
      <li>Sliding Scale: <i class="fas fa-balance-scale"></i></li>
    </ul>
     '''

    ## Columns to replace values in
    c2r = ['crisis', 'counseling', 'peer', 'health', 'addiction',
     'homelessness', 'advocacy', 'medication', 'other']

    for i in range(len(c2r)):
        df[c2r[i]] = df[c2r[i]].replace('Accessible physical location \[wheelchair and mobility aid accessible\]', '<i  class="fab fa-accessible-icon" title="accessible physical location"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Age specific limitations', '<i  class="fas fa-child" title="age specific limitations"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Firm costs', '<i  class="fas fa-comment-dollar" title="firm costs"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Free', '<i  class="fas fa-comment-dollar" title="free"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('LGBTQ Competent', '<i  class="fas fa-rainbow" title="LGBTQ competent"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Member only', '<i  class="fas fa-lock" title="member"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('No insurance required', '<i  class="fas fa-notes-medical" title="no insurance required"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Other', '<i  class="far fa-plus-square" title="other"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Remote/Online access', '<i  class="fas fa-globe" title="remote or online access"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace('Sliding Scale', '<i  class="fas fa-balance-scale" title="sliding scale"></i>', regex=True)
        df[c2r[i]] = df[c2r[i]].replace(',', '&nbsp;', regex=True)

    ## Replace newlines with HTML breaks
    df = df.replace({'\n': '<br>'}, regex=True)

    return fa_key, df

# ## Save df as an HTML table with customized style
# ## "display" is a data.tables default with striped rows
# ## you don't need table_id, but might be helpful for other iFrame approaches
# with open(filename, 'w') as f:
#     f.write(html_string.format(table=df.to_html(index=False, \
#      classes='display', escape=False, table_id="CRtable", na_rep=''), fa_key=fa_key))
#     f.close()

### Actual Run Code
if __name__ == "__main__":
    ## Render the HTML string
    html_string = setup_HTML()

    ## CSV approach
    csv_df = csv_approach(csv_file)
    ## Write a version based on CSV
    write_html('docs/CRDT-csv.html', html_string, csv_df)

    ## Google sheets approach
    gs_df = read_from_sheets(googleSheetID, worksheetName)
    gs_df = update_colnames(gs_df)
    ## Write a copy after cleaning the column names
    write_html('docs/CRDT-sheets.html', html_string, gs_df)

    ## Google sheets + Font Awesome
    fa_key, gs_df = awesomeify(gs_df)
    ## Write a copy after the Font Awesome substitutions
    write_html('docs/CRDT-sheets-FA.html', html_string, gs_df, fa_key)
