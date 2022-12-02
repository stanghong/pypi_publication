def quicklook(plot_df, curve1='lw_temp_3', curve2='Tbelow', *args, **kwargs):
    '''
    function to plot timeseries plot for QC purpose
    can select time window to see
    tbelow will be computed from ref_lwuw
    version 0.0.6
    example: 
        timetoseebegin='2022-06-09' 
        timetoseeend='2022-11-14'
        1. quick_look(plot_df, timetoseebegin, timetoseeend)
        2. quick_look1(test_df, timetoseebegin='10-15-2022', \
        timetoseeend='11-15-2022', curve1='Tbelow', curve2='prediction')
        
    '''
    #1. create copy of dataframe
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    plot_df=plot_df.set_index('time')
    
    timeflag=(plot_df.index>timetoseebegin) &  (plot_df.index<timetoseeend)
    if 'ref_lwuw' in plot_df.columns.tolist():
        plot_df['ref_tbelow']=(abs(plot_df['ref_lwuw'])/5.67e-8)**0.25-273.2
    

    for dev in plot_df.device.unique().tolist():
        ax=plot_df[(plot_df['device']==dev) & timeflag ][curve1].plot(color='red', title=f'{dev}',figsize=(12,4))
        ax2=plot_df[(plot_df['device']==dev) & timeflag ][curve2].plot( secondary_y=True, color='blue', ax=ax)
        ax.set_ylabel(f'{curve1}', color='red')
        ax2.set_ylabel(f'{curve2}', color='blue')

        ax.set_ylim(-10,70)
        ax2.set_ylim(-10,70)

        plt.show()
        
    #delete the temporary file for visualization
    plot_df.reset_index(drop=True)
