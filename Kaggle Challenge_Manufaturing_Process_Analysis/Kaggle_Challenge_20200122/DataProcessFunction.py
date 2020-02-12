
# coding: utf-8

# Calculate error rate (error versus setpoints)
def error_rate (data,actual,setpoint):
    
    result = (data[setpoint]-data[actual])/data[setpoint]

    result = result.round(3)

    return result

# Drop rows that have less than or equal to 0 output
def clean_outlier(data, col):
    
    data_new = data[(data[[col]] > 0).all(axis=1)]

    data_new.reset_index(drop=True, inplace=True)

    return data_new

# Calculate VIF (1/(1−R^2))
def vif_cal(input_data):
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    col_smallVif = []
    x_vars=input_data
    xvar_names=x_vars.columns
    for i in range(0,xvar_names.shape[0]):
        y=x_vars[xvar_names[i]] 
        x=x_vars[xvar_names.drop(xvar_names[i])]
        rsq=smf.ols(formula="y~x", data=x_vars).fit().rsquared  
        vif=round(1/(1-rsq),2)
        if vif < 10:
            col_smallVif.append(xvar_names[i])
        print (xvar_names[i], " VIF = " , vif)
        
    return col_smallVif

