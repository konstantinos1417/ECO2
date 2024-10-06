import pandas as pd
import folium
import geopandas as gpd
from branca.colormap import LinearColormap

sitesfile = 'csv_files\LAM_sites.csv'
ch4CIT = 'csv_files\CIT-2023-ch4.csv'
co2CIT = 'csv_files\CIT-2023-co2.csv'
ch4CNP = 'csv_files\CNP-2023-ch4.csv'
co2CNP = 'csv_files\CNP-2023-co2.csv'
ch4COM = 'csv_files\COM-2023-ch4-45m.csv'
co2COM = 'csv_files\COM-2023-co2-45m.csv'
ch4FUL = 'csv_files\FUL-2023-ch4.csv'
co2FUL = 'csv_files\FUL-2023-co2.csv'
ch4GRA = 'csv_files\GRA-2023-ch4-51m.csv'
co2GRA = 'csv_files\GRA-2023-co2-51m.csv'
ch4IRV = 'csv_files\IRV-2023-ch4.csv'
co2IRV = 'csv_files\IRV-2023-co2.csv'
ch4LJO = 'csv_files\LJO-2023-ch4-13m.csv'
co2LJO = 'csv_files\LJO-2023-co2-13m.csv'
ch4ONT = 'csv_files\ONT-2023-ch4-41m.csv'
co2ONT = 'csv_files\ONT-2023-co2-41m.csv'
ch4SCI = 'csv_files\SCI-2023-ch4-27m.csv'
co2SCI = 'csv_files\SCI-2023-co2-27m.csv'
ch4USC = r'csv_files\USC-2023-ch4.csv'
co2USC = r'csv_files\USC-2023-co2.csv'
ch4VIC = 'csv_files\VIC-2023-ch4-139m.csv'
co2VIC = 'csv_files\VIC-2023-co2-139m.csv'


#  csv reading
#
#
df = pd.read_csv(sitesfile)
df= df.drop(5)
df.at[4, 'SiteCode'] = 'USC'
df.at[4, 'SiteName'] = 'University of Southern California (downtown LA)'


dfco2CIT = pd.read_csv(co2CIT)
dfch4CIT = pd.read_csv(ch4CIT)

dfch4CNP= pd.read_csv(ch4CNP)
dfco2CNP=pd.read_csv(co2CNP)

dfch4FUL=pd.read_csv(ch4FUL)
dfco2FUL=pd.read_csv(co2FUL)

dfch4VIC=pd.read_csv(ch4VIC)
dfco2VIC=pd.read_csv(co2VIC)

dfch4IRV = pd.read_csv(ch4IRV)
dfco2IRV = pd.read_csv(co2IRV)

dfch4COM = pd.read_csv(ch4COM)
dfco2COM = pd.read_csv(co2COM)

dfch4GRA = pd.read_csv(ch4GRA)
dfco2GRA = pd.read_csv(co2GRA)

dfch4LJO = pd.read_csv(ch4LJO)
dfco2LJO = pd.read_csv(co2LJO)

dfch4ONT = pd.read_csv(ch4ONT)
dfco2ONT = pd.read_csv(co2ONT)

dfch4SCI = pd.read_csv(ch4SCI)
dfco2SCI = pd.read_csv(co2SCI)

dfch4USC = pd.read_csv(ch4USC)
dfco2USC = pd.read_csv(co2USC)
# csv heading
#
#
dfco2CIT.head()
dfch4CIT.head()

dfch4CNP.head()
dfco2CNP.head()

dfch4FUL.head()
dfco2FUL.head()

dfch4VIC.head()
dfco2VIC.head()

dfch4IRV.head()
dfco2IRV.head()

dfch4COM.head()
dfco2COM.head()

dfch4GRA.head()
dfco2GRA.head()

dfch4LJO.head()
dfco2LJO.head()

dfch4ONT.head()
dfco2ONT.head()

dfch4SCI.head()
dfco2SCI.head()

dfch4USC.head()
dfco2USC.head()

df.head()

map = folium.Map(location=[34.137,-118.126], tiles="cartodbpositron", min_zoom = 8)


sites = {
    'CIT': (dfch4CIT, dfco2CIT),
    'CNP': (dfch4CNP, dfco2CNP),
    'COM': (dfch4COM, dfco2COM),
    'FUL': (dfch4FUL, dfco2FUL),
    'GRA': (dfch4GRA, dfco2GRA),
    'IRV': (dfch4IRV, dfco2IRV),
    'LJO': (dfch4LJO, dfco2LJO),
    'ONT': (dfch4ONT, dfco2ONT),
    'SCI': (dfch4SCI, dfco2SCI),    
    'USC': (dfch4USC, dfco2USC),
    'VIC': (dfch4VIC, dfco2VIC),
    }

ch4avgs = []

linear = LinearColormap(["green","red"], vmin = 2100, vmax = 2180)
linear.caption = "CH4 emissions"
map.add_child(linear)

for ind in df.index:
    coords = df['Lat'][ind] , df['Lon'][ind]
    sitecode = df['SiteCode'][ind]
    sitename = df['SiteName'][ind]
    
    
    for key, (ch4_df, co2_df) in sites.items():
        if key in sitecode:
            ch4avg = ch4_df['ch4_ppb'].mean()
            co2avg = co2_df['co2_ppm'].mean()
            ch4max = ch4_df['ch4_max'].max()
            co2max = co2_df['co2_max'].max()
            break
        
    co2avg_str = f"{co2avg:.2f} ppm" 
    ch4avg_str = f"{ch4avg:.2f} ppb" 
    ch4max_str = f"{ch4max:.2f} ppb"
    co2max_str = f"{co2max:.2f} ppm"
    
    folium.Circle(location= coords, tooltip=sitename +" \n Average CH4 emissions:" +ch4avg_str, radius= 15000, color="black", weight=1, fill_opacity=0.8, fill_color=linear(ch4avg), fill=False).add_to(map)
    
    
    name = f"""
                <div style="width: 300px;">
                    <h1><b>{sitename}</b></h1><br>
                    <font size=4>
                    Site Code: <b>{sitecode}</b><br><br>
                    Average CO<sub>2</sub> (Carbon Dioxide) emissions recorded: <b>{co2avg_str}</b> <br><br>
                    Maximum CO<sub>2</sub> emission recorded: <b>{co2max_str}</b> <br><br>
                    Average CH<sub>4</sub> (Methane) emissions recorded: <b>{ch4avg_str}</b> <br><br>
                    Maximum CH<sub>4</sub> emission recorded: <b>{ch4max_str}</b></font> 
                </div>
            """
    
    folium.Marker(location = coords, popup = name,parse_html=True, max_width=300, icon=folium.Icon(icon="cloud", prefix="fa")).add_to(map)


map.save("map.html")