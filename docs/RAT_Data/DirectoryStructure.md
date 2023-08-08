# Directory Structure

Presented below is a detailed description of directories and files that are either used or generated by RAT {{rat_version.major}}.{{rat_version.minor}}.

!!! tip_note "Tip"
    Directories are represented by blue color, files are represented by purple color and the description of files/folder are represented by green color. 

<span class='data_folder'> RAT Project Directory (`project_dir`)</span>

<blockquote>

<details>
<p class='folder_file_description'> Conda environment folder for RAT with its python package and other dependencies. </p>
<summary><span class='data_folder'> .rat_env </span></summary>
</details>
<details>
<p class='folder_file_description'> Global database provided along with RAT and downloaded at the time of initialisation. Please note that this is the default location of the global database which can be changed at the time of initialisation by the flag `-gp or --global_data_dir`.</p>
<summary><span class='data_folder'> global_data </span></summary>
    <blockquote>
        <details>
            <summary><span class='data_folder'>global_altimetry</span></summary>
            <ul>
                <li><span class ='data_file'>geoidegm2008grid.mat</span></li>
                <li><span class ='data_file'>j3_tracks.geojson  </span></li>
            </ul>
        </details>
        <details>
            <summary><span class='data_folder'>global_basin_data</span></summary>
            <ul>
                <li><span class ='data_file'>GRDC Major River Basins.pdf</span></li>
                <li><span class ='data_file'>MRB TECHDOC.pdf</span></li>
            </ul>
            <blockquote style="margin-top:-25px;">
                <details>
                    <summary><span class='data_folder'>shapefiles</span></summary>
                    <ul>
                        <li><span class ='data_file'>mrb_basins.json</span></li>
                        <li><span class ='data_file'>mrb_rivers.json</span></li>
                    </ul>
                </details>
            </blockquote>   
        </details>
        <details>
            <summary><span class='data_folder'>global_dam_data</span></summary>
            <ul>
                <li><span class ='data_file'>GRanD_dams_v1_3_filtered.shp</span></li>
                <li><span class ='data_file'>GRanD_dams_v1_3_filtered.dbf</span></li>
                <li><span class ='data_file'>GRanD_dams_v1_3_filtered.prj</span></li>
                <li><span class ='data_file'>GRanD_dams_v1_3_filtered.shp</span></li>
                <li><span class ='data_file'>GRanD_dams_v1_3_filtered.shx</span></li>
            </ul>
        </details>
        <details>
            <p class='folder_file_description'> Even though hydrosheds flow direction file is provided, it is not used due to lower spatial resolution.</p>
            <summary><span class='data_folder'>global_drt_flow_file</span></summary>
            <ul>
                <li><span class ='data_file'>global_drt_flow_16th.tif</span></li>
                <li><span class ='data_file'>hyd_glo_dir_30s.tif</span></li>
                <li><span class ='data_file'>HydroSHEDS_TechDoc_v1_4.pdf</span></li>
            </ul>
        </details>
        <details>
            <summary><span class='data_folder'>global_elevation_data</span></summary>
            <ul>
                <li><span class ='data_file'>World_e-Atlas-UCSD_SRTM30-plus_v8.tif</span></li>
            </ul>
        </details>
        <details>
            <p class='folder_file_description'> Unfiltered and original version of GRanD database of dams and reservoirs.</p>
            <summary><span class='data_folder'>global_grand_data</span></summary>
            <ul>
                <li><span class ='data_file'>GRanD_dams_v1_3.shp</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.shp</span></li>
            </ul>
        </details>
        <details>
            <summary><span class='data_folder'>global_reservoir_data</span></summary>
            <ul>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.shp</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.prj</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.dbf</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.sbx</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.shx</span></li>
                <li><span class ='data_file'>GRanD_reservoirs_v1_3.sbn</span></li>
            </ul>
        </details>
        <details>
            <summary><span class='data_folder'>global_vic_params</span></summary>
            <ul>
                <li><span class ='data_file'>africa_domain.nc</span></li>
                <li><span class ='data_file'>africa_params.nc</span></li>
                <li><span class ='data_file'>australia_domain.nc</span></li>
                <li><span class ='data_file'>australia_params.nc</span></li>
                <li><span class ='data_file'>eurasia_domain.nc</span></li>
                <li><span class ='data_file'>eurasia_params.nc</span></li>
                <li><span class ='data_file'>kamchatka_domain.nc</span></li>
                <li><span class ='data_file'>kamchatka_params.nc</span></li>
                <li><span class ='data_file'>namerica_domain.nc</span></li>
                <li><span class ='data_file'>namerica_params.nc</span></li>
                <li><span class ='data_file'>samerica_domain.nc</span></li>
                <li><span class ='data_file'>samerica_params.nc</span></li>
                <li><span class ='data_file'>oceania_domain.nc</span></li>
                <li><span class ='data_file'>oceania_params.nc</span></li>
            </ul>
        </details>
    </blockquote>
</details>
<details>
<p class='folder_file_description'> It contains the hydrological models which are used by RAT to estimate inflow.</p>
<summary><span class='data_folder'> models </span></summary>
    <blockquote>
        <details>
            <p class='folder_file_description'> It is the python based conda environment which is used to execute MetSim. It is installed during initialization.</p>
            <summary><span class='data_folder'>metsim</span></summary>
        </details>
        <details>
            <p class='folder_file_description'> It is the python based conda environment which is used to execute VIC. It is installed during initialization. It also has the VIC executables for classic and image driver but RAT uses only image driver.</p>
            <summary><span class='data_folder'>vic</span></summary>
            <ul>
                <li><span class ='data_file'>vic_classic.exe</span></li>
                <li><span class ='data_file'>vic_image.exe</span></li>
            </ul>
        </details>
        <details>
            <p class='folder_file_description'> It contains the fortran code for routing and also has the compiled code, file required to compile the code (makefile). It is downloaded and installed during initialization.</p>
            <summary><span class='data_folder'>routing</span></summary>
            <ul>
                <li><span class ='data_file'>rout.o</span></li>
                <li><span class ='data_file'>rout.f</span></li>
                <li><span class ='data_file'>rout</span></li>
                <li><span class ='data_file'>makefile</span></li>
            </ul>
        </details>
    </blockquote>
</details>
<details>
<p class='folder_file_description'> It contains the default parameter files and configuration templates for RAT and the hydrological model which are used by it.</p>
<summary><span class='data_folder'> params </span></summary>
    <blockquote>
        <ul style="margin-left:-5px;margin-bottom:0px;">
            <li><span class ='data_file'>basins_metadata_texas.csv</span></li>
            <li><span class ='data_file'>MRB TECHDOC.pdf</span></li>
        </ul>
        <details>
            <p class='folder_file_description'> It contains configuration file required to run MetSim. It is updated everytime RAT runs MetSim.</p>
            <summary><span class='data_folder'>metsim</span></summary>
            <ul>
                <li><span class ='data_file'>params.yaml</span></li>
            </ul>
        </details>
        <details>
            <p class='folder_file_description'> It contains parameter configuration file required to run VIC. It is updated everytime RAT runs VIC.</p>
            <summary><span class='data_folder'>vic</span></summary>
            <ul>
                <li><span class ='data_file'>vic_params.txt</span></li>
            </ul>
        </details>
        <details>
            <p class='folder_file_description'> It contains parameter configuration file required to run routing. It is updated everytime RAT runs VIC. It also contains the default standard unit hydrograph file used by RAT.</p>
            <summary><span class='data_folder'>routing</span></summary>
            <ul>
                <li><span class ='data_file'>route_param.txt</span></li>
                <li><span class ='data_file'>uh.txt</span></li>
            </ul>
        </details>
    </blockquote>
</details>
<details>
<p class='folder_file_description'> It contains all the data produced and generated by RAT. Other than that it contains log files for debugging, test data and outputs of test data. Please note it is just the default location of data directory which can be changed by <code>data_dir</code> parameter in the configuration file.</p>
<summary><span class='data_folder'> data (<code>data_dir</code>) </span></summary>
    <blockquote>
        <details>
            <summary><span class='data_folder'>raw</span></summary>
            <blockquote>
                <details>
                    <p class='folder_file_description'> It contains global precipitation files downloaded from IMERG in geotif format. Each file is named according to the date of which it contains the data.</p>
                    <summary><span class='data_folder'>precipitation</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global maximum temperature files downloaded from NOAA in NetCDF format. Each file is named according to the year of which it contains the data.</p>
                    <summary><span class='data_folder'>tmax</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global minimum temperature files downloaded from NOAA in NetCDF format. Each file is named according to the year of which it contains the data.</p>
                    <summary><span class='data_folder'>tmin</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global u direction wind speed files downloaded from NOAA in NetCDF format. Each file is named according to the year of which it contains the data. The data is present at a frequency of 6 hours.</p>
                    <summary><span class='data_folder'>uwnd</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global v direction wind speed files downloaded from NOAA in NetCDF format. Each file is named according to the year of which it contains the data. The data is present at a frequency of 6 hours.</p>
                    <summary><span class='data_folder'>vwnd</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global u direction wind speed files where data is availale at daily frequency created from 6 hourly files. Each file is named according to the year of which it contains the data.</p>
                    <summary><span class='data_folder'>uwnd_daily</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains global v direction wind speed files where data is availale at daily frequency created from 6 hourly files. Each file is named according to the year of which it contains the data.</p>
                    <summary><span class='data_folder'>vwnd_daily</span></summary>
                </details>
            </blockquote>  
        </details>
        <details>
            <p class='folder_file_description'> It contains brief level (level-1) log file corresponding to the user's RAT execution, providing concise information on the successful execution of each step for each basin, along with any associated errors.</p>
            <summary><span class='data_folder'>runs</span></summary>
            <blockquote>
                <details>
                    <p class='folder_file_description'> Level-1 log files are named by the convention RAT_run-&lt;date-time&gt;.log.</p>
                    <summary><span class='data_folder'>logs</span></summary>
                </details>
            </blockquote>
        </details>
        <details>
            <p class='folder_file_description'> It contains data required to test the installation, initialization and working  of RAT for test basins. It is downloaded by the <code>rat test</code> command.</p>
            <summary><span class='data_folder'>test_data</span></summary>
            <blockquote>
                <details>
                    <p class='folder_file_description'>  It contains data required to test RAT execution for the test basin - Gunnison.</p>
                    <summary><span class='data_folder'>gunnison</span></summary>
                </details>
                <details>
                    <p class='folder_file_description'> It contains data required to test RAT execution for the test basin - Nueces.</p>
                    <summary><span class='data_folder'>Nueces</span></summary>
                </details>
            </blockquote>
        </details>
        <details>
            <p class='folder_file_description'> It is a replication of <code> data_dir</code> and contains RAT generated data for test basins by using <code>rat test</code> command.</p>
            <summary><span class='data_folder'>test_output</span></summary>
        </details>
        <details>
            <summary><span class='data_folder'><code>region_name</code></span></summary>
            <blockquote>
                <details>
                    <p class='folder_file_description'> It contains RAT produced output data for different basins having the same <code>region_name</code>.</p>
                    <summary><span class='data_folder'>basins</span></summary>
                    <blockquote>
                        <details>
                            <p class='folder_file_description'> It contains RAT produced output data for one basin with name <code>basin_name</code>.</p>
                            <summary><span class='data_folder'><code>basin_name</code></span></summary>
                            <blockquote>
                                <details>
                                    <p class='folder_file_description'> It contains river basin's grid file and a river basin mask in Geotif format at a spatial resolution of 0.0625&deg;.</p>
                                    <summary><span class='data_folder'><code>basin_grid_data</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains preprocessed meteorological data for this particular basin only after scaling, aligning and clipping in 'processed' folder. Also, all this meteorological data is combined into a single NetCDF file and is stored in 'nc' folder. This signle file is used to prepare MetSim inputs.</p>
                                    <summary><span class='data_folder'><code>pre_processing</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all data related to MetSim generated by RAT.</p>
                                    <summary><span class='data_folder'><code>metsim</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all data related to VIC generated by RAT.</p>
                                    <summary><span class='data_folder'><code>vic</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all data related to Routing generated by RAT.</p>
                                    <summary><span class='data_folder'><code>ro</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all data related to Google Eearth Engine (GEE) and surface area computations generated by RAT.</p>
                                    <summary><span class='data_folder'><code>gee</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all data related to altimetry elevation extraction of reservoirs generated by RAT.</p>
                                    <summary><span class='data_folder'><code>altimetry</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all Area Elevation Curves of reservoirs generated by RAT. Please note that it is the default location which can be changed by <code>aec_dir</code> in the RAT configuration file.</p>
                                    <summary><span class='data_folder'><code>post_processing</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all the outputs generated by RAT in detail.</p>
                                    <summary><span class='data_folder'><code>rat_outputs</code></span></summary>
                                </details>
                                <details>
                                    <p class='folder_file_description'> It contains all the final outputs polished and in time-series format generated by RAT. Users are recommended to use these outputs for further analysis.</p>
                                    <summary><span class='data_folder'><code>final_outputs</code></span></summary>
                                </details>
                            </bloackquote>
                        </details>
                    </bloackquote>
                </details>
                <details>
                    <p class='folder_file_description'> It contains detailed level (level-2) log file corresponding to a basin for which RAT has been executed and offers a comprehensive description of the computations and processes undertaken by RAT for that basin</p>
                    <summary><span class='data_folder'>logs</span></summary>
                    <blockquote>
                        <details>
                            <p class='folder_file_description'> It contains level-2 logs for one basin with name <code>basin_name</code>. The log files are named as RAT-<code>basin_name</code>date-time.log.</p>
                            <summary><span class='data_folder'><code>basin_name</code></span></summary>
                        </details>
                    </bloackquote>
                </details>
                <details>
                    <p class='folder_file_description'> It contains log files generated by VIC when it is executed by RAT.</p>
                    <summary><span class='data_folder'>vic_logs</span></summary>
                    <blockquote>
                        <details>
                            <p class='folder_file_description'> It contains vic logs for one basin with name <code>basin_name</code>. The log files are named as vic.log.date-time.txt.</p>
                            <summary><span class='data_folder'><code>basin_name</code></span></summary>
                        </details>
                    </bloackquote>
                </details>
            </blockquote>  
        </details>
    </blockquote>
</details>