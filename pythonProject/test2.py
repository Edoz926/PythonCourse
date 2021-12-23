import datetime

db_ref = 'BillingCenter'

# Set Quantitative Data calculation parameter
# Dates to find triggers (edit, will be substituted by today in workflow use)
selectedDates = ['2021-08-11', '2021-02-10']
today = datetime.datetime.today().strftime('%Y-%m-%d')

print(f"======> Selected Dates: {selectedDates}")

# FRAME LIST USED TO PERFORM MULTIPLE DAYS CALCULATION
# IT WILL BE MERGED AT THE END
frameList = []

# the first part brings out the movements (issue, policychange, cancellations, etc.)
# that must be triggered by the SITA.
# In the second step (Billing tables)
# the payments of the half-yearly installments are
# joined with the last JOB created because this movement must also be triggered.

# !!!!!!!!!!!!
# Requirements
# !!!!!!!!!!!!

# PART 1
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# This is the default case that returns null.

# PART2
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# This is the default case that returns null.

# PART3
# In the case of PolicyChange in which al least one of the key fields is changed,
# a second record must be sent to ANIA related to the previous period.
# In the case in which the effective date is the same of previous period, the A-0 record must be sent.
# Instead in the case in which the effective date is different of previous period, the I-2 record must be sent.

# PART4

# In the case of Submission,
# only 1 record must be sent (related to current period).
# In the case the client pay the next installment,
# only 1 record must be sent (related to current period).
# In the case of Renewal,
# only 1 record must be sent (related to current period).
# In the case of Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).
# In the case of PolicyChange in which al least one of the key fields is changed,
# 2 records must be sent (first one is related to current period and the second one is related to the previous period).
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# only 1 record must be sent (related to current period).
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).
# This is the default case that returns null.

# PART 5-6-7-8
# This will be used later inside the filters
# return annual policies
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed,
# a second record must be sent to ANIA related to the previous period.
# In the case in which the effective date is the same of previous period, the A-0 record must be sent.
# Instead in the case in which the effective date is different of previous period, the I-2 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed,
# a second record must be sent to ANIA related to the previous period.
# In the case in which the effective date is the same of previous period, the A-0 record must be sent.
# Instead in the case in which the effective date is different of previous period, the I-2 record must be sent.
# In the case of Submission,
# only 1 record must be sent (related to current period).
# In the case the client pay the next installment,
# only 1 record must be sent (related to current period).
# In the case of Renewal,
# only 1 record must be sent (related to current period).
# In the case of Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).
# 2 records must be sent (first one is related to current period and the second one is related to the previous period).
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# only 1 record must be sent (related to current period).
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).

# PART 5-6-7-8
# This will be used later inside the filters
# return annual policies
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# In the case of Submission, the C-0 record must be sent.
# In the case the client pay the next installment, the C-0 record must be sent.
# In the case of Renewal, the C-0 record must be sent.
# In the case of Suspension (except for 'Morosita' reason), the I-3 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed, the C-0 record must be sent.
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# the A-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# the I-1 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# the I-4 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# the I-5 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# the I-9 record must be sent.
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# the I-6 record must be sent.
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason), the C-1 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed,
# a second record must be sent to ANIA related to the previous period.
# In the case in which the effective date is the same of previous period, the A-0 record must be sent.
# Instead in the case in which the effective date is different of previous period, the I-2 record must be sent.
# In the case of PolicyChange in which al least one of the key fields is changed,
# a second record must be sent to ANIA related to the previous period.
# In the case in which the effective date is the same of previous period, the A-0 record must be sent.
# Instead in the case in which the effective date is different of previous period, the I-2 record must be sent.
# In the case of Submission,
# only 1 record must be sent (related to current period).
# In the case the client pay the next installment,
# only 1 record must be sent (related to current period).
# In the case of Renewal,
# only 1 record must be sent (related to current period).
# In the case of Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).
# 2 records must be sent (first one is related to current period and the second one is related to the previous period).
# In the case of Cancellation with same effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForA1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI1,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI4,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI5,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI9,
# only 1 record must be sent (related to current period).
# In the case of Cancellation with different effective date of previous period
# and a specific cancellation reason defined in CancellationReasonCodeForI6,
# only 1 record must be sent (related to current period).
# In the case of Reactivation generated after a Suspension (except for 'Morosita' reason),
# only 1 record must be sent (related to current period).

# RETRIVE
# Retrive utility data
# This will be used later inside the filters
# return TRIGGERED policies
# Returns
# ID_Policy_PC
# number policy
# close trasmission date
# triggered movement type
# triggered notification id
# triggered cause code
# previous triggered movement type
# previous triggered notification id
# previous triggered cause code
# ID_Policy_PC
# Ania vehicle type
# TaxIDInternal policyHolder
# CompanyNameInternal policyHolder
# FirstNameInternal policyHolder
# LastNameInternal policyHolder
# TaxIDInternal policyHolder
# CompanyNameInternal policyHolder
# TaxIDInternal vehicleOwner
# CompanyNameInternal vehicleOwner
# FirstNameInternal vehicleOwner
# LastNameInternal vehicleOwner
# TaxIDInternal vehicleOwner
# CompanyNameInternal vehicleOwner


for selectedDate in selectedDates:
    querona = f"""
        (SELECT  Base.ID_Policy_PC AS    Base_ID_Policy_PC,
            Base.ID_PolicyPeriod_PC AS  Base_ID_PolicyPeriod_PC,
            Base.JobNumber AS   Base_JobNumber,
            Base.Data_Chiusura_Transazione AS   Base_Data_Chiusura_Transazione,
            Base.PolicyChangeReasonCode AS  Base_PolicyChangeReasonCode,
            Base.Numero_Polizza AS      Base_Numero_Polizza, 
            Base.RegistrationNumber AS  Base_RegistrationNumber,

            case when (Base.IsSubmission = 1)
                    then 'C'
                when (Base.IsNextInstallment = 1)
                    then 'C'
                when (Base.IsRenewal = 1)
                    then 'C'
                when (Base.IsSuspension = 1 and Base.SuspensionTypeToInclude = 1)
                    then 'I'
                when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1 and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA))
                    then 'C'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate = Previous.EditEffectiveDate and Base.CancellationReasonCodeForA1 = 1)
                    then 'A'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI1 = 1)
                    then 'I'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI4 = 1)
                    then 'I'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI5 = 1)
                    then 'I'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI9 = 1)
                    then 'I'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI6 = 1)
                    then 'I'
                when (Base.IsReactivation = 1 and Suspensions.SuspensionTypeToInclude = 1)
                    then 'C'
                else Base.TipoMovimento end AS Base_TipoMovimento,

            case when (Base.IsSubmission = 1)
                    then '0'
                when (Base.IsNextInstallment = 1)
                    then '0'
                when (Base.IsRenewal = 1)
                    then '0'
                when (Base.IsSuspension = 1 )
                    then '3'
                when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1 and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA))
                    then '0'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate = Previous.EditEffectiveDate and Base.CancellationReasonCodeForA1 = 1)
                    then '1'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI1 = 1)
                    then '1'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI4 = 1)
                    then '4'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI5 = 1)
                    then '5'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI9 = 1)
                    then '9'
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI6 = 1)
                    then '6'
                when (Base.IsReactivation = 1 and Suspensions.SuspensionTypeToInclude = 1)
                    then '1'
                else Base.CausaleMovimento end AS Base_CausaleMovimento,

            case when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1
                    and (Base.EditEffectiveDate = Previous.EditEffectiveDate AND Base.ChangeVehicleHour = Previous.ChangeVehicleHour)
                    and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA)
                    ) then 'A'
                when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1
                    and (Base.EditEffectiveDate != Previous.EditEffectiveDate OR Base.ChangeVehicleHour != Previous.ChangeVehicleHour)
                    and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA)
                    ) then 'I'
                else Base.TipoMovimentoPrecedente end AS Base_TipoMovimentoPrecedente,

            case when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1
                    and (Base.EditEffectiveDate = Previous.EditEffectiveDate AND Base.ChangeVehicleHour = Previous.ChangeVehicleHour)
                    and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA)
                    ) then '0'
                when (Base.IsPolicyChange = 1 and Base.PolicyChangeReasonCodeToExclude = 1
                    and (Base.EditEffectiveDate != Previous.EditEffectiveDate OR Base.ChangeVehicleHour != Previous.ChangeVehicleHour)
                    and (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA)
                    ) then '2'
                else Base.CausaleMovimentoPrecedente end AS Base_CausaleMovimentoPrecedente,

            case when (Base.IsSubmission = 1)
                    then 1
                when (Base.IsNextInstallment = 1)
                    then 1
                when (Base.IsRenewal = 1)
                    then 1
                when (Base.IsSuspension = 1)
                    then 1
                when (Base.IsPolicyChange = 1 and 
                Base.PolicyChangeReasonCodeToExclude = 1 and 
                (Base.Numero_Polizza != Previous.Numero_Polizza OR Base.RegistrationNumber != Previous.RegistrationNumber OR Base.TaxIDInternalContraentePolizza != Previous.TaxIDInternalContraentePolizza OR Base.NomeCompagniaContraentePolizza != Previous.NomeCompagniaContraentePolizza OR Base.NomeContraentePolizza != Previous.NomeContraentePolizza OR Base.CognomeContraentePolizza != Previous.CognomeContraentePolizza OR Base.TaxIDInternalProprietarioVeicolo != Previous.TaxIDInternalProprietarioVeicolo OR Base.NomeCompagniaProprietarioVeicolo != Previous.NomeCompagniaProprietarioVeicolo OR Base.NomeContraenteProprietarioVeicolo != Previous.NomeContraenteProprietarioVeicolo OR Base.CognomeContraenteProprietarioVeicolo != Previous.CognomeContraenteProprietarioVeicolo OR Base.Codice_IUR != Previous.Codice_IUR OR Base.BlackBox != Previous.BlackBox OR Base.TipoVeicoloANIA != Previous.TipoVeicoloANIA))
                    then 2
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate = Previous.EditEffectiveDate and Base.CancellationReasonCodeForA1 = 1)
                    then 1
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI1 = 1)
                    then 1
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI4 = 1)
                    then 1
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI5 = 1)
                    then 1
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI9 = 1)
                    then 1
                when (Base.IsCancellation = 1 and Base.EditEffectiveDate != Previous.EditEffectiveDate and Base.CancellationReasonCodeForI6 = 1)
                    then 1
                when (Base.IsReactivation = 1 and Suspensions.SuspensionTypeToInclude = 1)
                    then 1
                else Base.NumeroTrigger end AS Base_NumeroTrigger,

            Base.NotificationID_Triggerato AS   Base_NotificationID_Triggerato,
            Base.NotificationChannel_Triggerato AS  Base_NotificationChannel_Triggerato,
            Base.TipoMovimento_Triggerato AS    Base_TipoMovimento_Triggerato,
            Base.CausaleMovimento_Triggerato AS     Base_CausaleMovimento_Triggerato,
            Base.NotificaStatus_Triggerato AS   Base_NotificaStatus_Triggerato,
            Base.NotificationPrecedenteID_Triggerato AS     Base_NotificationPrecedenteID_Triggerato,
            Base.NotificationPrecedenteChannel_Triggerato AS    Base_NotificationPrecedenteChannel_Triggerato,
            Base.TipoMovimentoPrecedente_Triggerato AS  Base_TipoMovimentoPrecedente_Triggerato,
            Base.CausaleMovimentoPrecedente_Triggerato AS   Base_CausaleMovimentoPrecedente_Triggerato,
            Base.NotificaStatusPrecedente_Triggerato AS     Base_NotificaStatusPrecedente_Triggerato,
            Base.NumeroTrigger_Triggerato AS    Base_NumeroTrigger_Triggerato,
            Base.TaxIDInternalContraentePolizza AS  Base_TaxIDInternalContraentePolizza,
            Base.NomeCompagniaContraentePolizza AS  Base_NomeCompagniaContraentePolizza,
            Base.NomeContraentePolizza AS   Base_NomeContraentePolizza,
            Base.CognomeContraentePolizza AS    Base_CognomeContraentePolizza,
            Base.TaxIDInternalProprietarioVeicolo AS    Base_TaxIDInternalProprietarioVeicolo,
            Base.NomeCompagniaProprietarioVeicolo AS    Base_NomeCompagniaProprietarioVeicolo,
            Base.NomeContraenteProprietarioVeicolo AS   Base_NomeContraenteProprietarioVeicolo, 
            Base.CognomeContraenteProprietarioVeicolo AS    Base_CognomeContraenteProprietarioVeicolo,
            Base.Codice_IUR AS      Base_Codice_IUR, 
            Base.BlackBox AS    Base_BlackBox,
            Base.TipoVeicoloANIA AS     Base_TipoVeicoloANIA,
            Base.EditEffectiveDate AS   Base_EditEffectiveDate,
            Base.ChangeVehicleHour AS   Base_ChangeVehicleHour,

            Previous.ID_Policy_PC AS    Previous_ID_Policy_PC,
            Previous.ID_PolicyPeriod_PC AS  Previous_ID_PolicyPeriod_PC,
            Previous.JobNumber AS   Previous_JobNumber,
            Previous.Data_Chiusura_Transazione AS   Previous_Data_Chiusura_Transazione,
            Previous.Numero_Polizza AS      Previous_Numero_Polizza, 
            Previous.RegistrationNumber AS  Previous_RegistrationNumber,
            Previous.TaxIDInternalContraentePolizza AS  Previous_TaxIDInternalContraentePolizza,
            Previous.NomeCompagniaContraentePolizza AS  Previous_NomeCompagniaContraentePolizza,
            Previous.NomeContraentePolizza AS   Previous_NomeContraentePolizza,
            Previous.CognomeContraentePolizza AS    Previous_CognomeContraentePolizza,
            Previous.TaxIDInternalProprietarioVeicolo AS    Previous_TaxIDInternalProprietarioVeicolo,
            Previous.NomeCompagniaProprietarioVeicolo AS    Previous_NomeCompagniaProprietarioVeicolo,
            Previous.NomeContraenteProprietarioVeicolo AS   Previous_NomeContraenteProprietarioVeicolo, 
            Previous.CognomeContraenteProprietarioVeicolo AS    Previous_CognomeContraenteProprietarioVeicolo,
            Previous.Codice_IUR AS      Previous_Codice_IUR, 
            Previous.BlackBox AS    Previous_BlackBox,
            Previous.TipoVeicoloANIA AS     Previous_TipoVeicoloANIA,
            Previous.EditEffectiveDate AS   Previous_EditEffectiveDate,
            Previous.ChangeVehicleHour AS   Previous_ChangeVehicleHour,

            Suspensions.ID_Policy_PC AS     Suspensions_ID_Policy_PC,
            Suspensions.ID_PolicyPeriod_PC AS   Suspensions_ID_PolicyPeriod_PC,
            Suspensions.Data_Chiusura_Transazione AS    Suspensions_Data_Chiusura_Transazione,
            Suspensions.Numero_Polizza AS   Suspensions_Numero_Polizza, 
            Suspensions.SuspensionTypeToInclude AS  Suspensions_SuspensionTypeToInclude,

            rank() over (partition by Base.ID_PolicyPeriod_PC
                         order by Base.Data_Chiusura_Transazione desc,
                                  Previous.Data_Chiusura_Transazione desc,
                                  Suspensions.Data_Chiusura_Transazione desc) as idrank,

            current_timestamp as ref_dts,
            '{selectedDate}' as ref_day_dts
    FROM (

        SELECT          policyperiod_0.PolicyID                                                             ID_Policy_PC,
                        policyperiod_0.ID                                                                   ID_PolicyPeriod_PC,
                        job_2.JobNumber                                                                     JobNumber,
                        job_2.CloseDate                                                                     Data_Chiusura_Transazione,
                        PolicyChangeReason.ReasonTypecode                                                   PolicyChangeReasonCode,
                        policyperiod_0.policynumber                                                         Numero_Polizza, 
                        gRoot.RegistrationNumber                                                            RegistrationNumber,
                        null                                                                                TipoMovimento,
                        null                                                                                CausaleMovimento,
                        null                                                                                TipoMovimentoPrecedente,
                        null                                                                                CausaleMovimentoPrecedente,
                        0                                                                                   NumeroTrigger,
                        SITANotification.ID                                                                 NotificationID_Triggerato,
                        SITANotification.TransmissionChannel                                                NotificationChannel_Triggerato,
                        SITANotification.MovementType                                                       TipoMovimento_Triggerato,
                        SITANotification.CauseCode                                                          CausaleMovimento_Triggerato,
                        SITANotificationStatus.TYPECODE                                                     NotificaStatus_Triggerato,
                        SITANotificationPrevious.ID                                                         NotificationPrecedenteID_Triggerato,
                        SITANotificationPrevious.TransmissionChannel                                        NotificationPrecedenteChannel_Triggerato,
                        SITANotificationPrevious.MovementType                                               TipoMovimentoPrecedente_Triggerato,
                        SITANotificationPrevious.CauseCode                                                  CausaleMovimentoPrecedente_Triggerato,
                        SITANotificationPreviousStatus.TYPECODE                                             NotificaStatusPrecedente_Triggerato,
                        case when (SITANotification.MovementType is not null
                                and SITANotificationPrevious.MovementType is not null) then 2
                            when (SITANotification.MovementType is not null
                                and SITANotificationPrevious.MovementType is null) then 1
                            else 0
                        end                                                                                 NumeroTrigger_Triggerato,
                        policyHolder_1.TaxIDInternal                                                        TaxIDInternalContraentePolizza,
                        policyHolder_1.CompanyNameInternal                                                  NomeCompagniaContraentePolizza,
                        policyHolder_1.FirstNameInternal                                                    NomeContraentePolizza,
                        policyHolder_1.LastNameInternal                                                     CognomeContraentePolizza,
                        vehicleOwner_1.TaxIDInternal                                                        TaxIDInternalProprietarioVeicolo,
                        vehicleOwner_1.CompanyNameInternal                                                  NomeCompagniaProprietarioVeicolo,
                        vehicleOwner_1.FirstNameInternal                                                    NomeContraenteProprietarioVeicolo, 
                        vehicleOwner_1.LastNameInternal                                                     CognomeContraenteProprietarioVeicolo,
                        iurcode_ait_11.code                                                                 Codice_IUR, 
                        CASE WHEN vehicleCoverage_Vehicle.Vehicle IS NOT NULL   THEN 1 ELSE 0 END           BlackBox,
                        case when (vehicleType.TYPECODE = 'car')        then 'A'
                             when (vehicleType.TYPECODE = 'motorcycle') then 'M'
                             when (vehicleType.TYPECODE = 'moped')      then 'W'
                             else null end                                                                  TipoVeicoloANIA,

                        case when (jobSubtype.TYPECODE = 'Submission') then 1 else 0 end                    IsSubmission,
                        0                                                                                   IsNextInstallment,
                        case when (jobSubtype.TYPECODE = 'Renewal') then 1 else 0 end                       IsRenewal,
                        case when (jobSubtype.TYPECODE = 'PolicyChange') then 1 else 0 end                  IsPolicyChange,
                        case when (jobSubtype.TYPECODE = 'PolicyChange'
                            and Operation.TYPECODE = 'suspensionPolicy') then 1 else 0 end                  IsSuspension,
                        case when (suspensionType.TYPECODE in (
                                'volontaria',
                                'richiesta_compagnia')) then 1 else 0 end                                   SuspensionTypeToInclude,
                        (CASE WHEN (jobSubtype.TYPECODE = 'PolicyChange'
                            and Operation.TYPECODE = 'reactivationPolicy') THEN 1 ELSE 0 END)               IsReactivation,
                        case when (jobSubtype.TYPECODE = 'Cancellation') then 1 else 0 end                  IsCancellation,
                        case when (cancellationReasonCode.TYPECODE in (
                            'totalloss',
                            'sold',
                            'accountsold',
                            'withdrawalforreconsideration',
                            'demolitiondestruction',
                            'export',
                            'deathoftheowner',
                            'wihouteffect',
                            'nottaken')) then 1 else 0 end                                                  CancellationReasonCodeForA1,
                        case when (cancellationReasonCode.TYPECODE in (
                            'totalloss')) then 1 else 0 end                                                 CancellationReasonCodeForI1,
                        case when (cancellationReasonCode.TYPECODE in (
                            'sold',
                            'accountsold')) then 1 else 0 end                                               CancellationReasonCodeForI4,
                        case when (cancellationReasonCode.TYPECODE in (
                            'withdrawalforreconsideration')) then 1 else 0 end                              CancellationReasonCodeForI5,
                        case when (cancellationReasonCode.TYPECODE in (
                            'demolitiondestruction',
                            'export')) then 1 else 0 end                                                    CancellationReasonCodeForI9,
                        case when (cancellationReasonCode.TYPECODE in (
                            'deathoftheowner')) then 1 else 0 end                                           CancellationReasonCodeForI6,
                        case when (PolicyChangeReason.ReasonTypecode not in (
                            'AggiuntaVeicoloMulticar',
                            'AnnulloCoperturaVeicoloMulticar',
                            'GestionePortafoglio',
                            'InizializzazioneATR',
                            'RettificaATR',
                            'TermExpirationExtension')) then 1 else 0 end                                   PolicyChangeReasonCodeToExclude,

                        convert(date, policyperiod_0.EditEffectiveDate)                                     EditEffectiveDate,                  
                        REPLACE(CONVERT(varchar(5), gRoot.ChangeVehicleHour, 108), ':', '')                 ChangeVehicleHour,

                        1                                                                                   idrank

        FROM            pcx_vehicle_ait gRoot 
        INNER JOIN      pc_policyperiod AS policyperiod_0 ON policyperiod_0.id=groot.branchid 
        INNER JOIN      pc_policy       AS policy_1 ON policy_1.id=policyperiod_0.policyid 
        LEFT  JOIN      pcx_iurcode_ait AS iurcode_ait_11 ON groot.id=iurcode_ait_11.vehicle
        INNER JOIN      pc_job AS job_2 ON job_2.id=policyperiod_0.jobid
        INNER JOIN      pc_policyline AS policyline_0 ON policyperiod_0.ID = policyline_0.BranchID 
        LEFT JOIN       (SELECT DISTINCT vehicleCoverage.Vehicle as Vehicle
                         FROM            pcx_vehiclecov_ait vehicleCoverage
                         WHERE           vehicleCoverage.ExpirationDate IS NULL
                         AND             vehicleCoverage.PatternCode = 'A009') vehicleCoverage_Vehicle ON gRoot.ID = vehicleCoverage_Vehicle.Vehicle
        LEFT JOIN       pctl_suspensiontype_ait suspensionType ON suspensionType.ID = job_2.SuspensionType_AIT
        LEFT JOIN       pctl_reasoncode cancellationReasonCode ON cancellationReasonCode.ID = job_2.CancelReasonCode
        INNER JOIN      pctl_job as jobSubtype ON jobSubtype.ID = job_2.subtype
        INNER JOIN      pctl_mtvehicletype_ait as vehicleType ON vehicleType.ID = groot.vehicletype 


        LEFT JOIN       (SELECT policyperiod_3.ID as policyperiod_3ID,
                                MAX(policyHolder_0.ID) policyHolderID
                                FROM pc_policycontactrole policyHolder_0 
                                INNER JOIN pc_policyperiod AS policyperiod_3 ON policyperiod_3.id=policyHolder_0.branchid 
                                WHERE policyHolder_0.subtype = (SELECT TOP 1 ID FROM pctl_policycontactrole WHERE TYPECODE = 'PolicyPriNamedInsured')
                                AND policyperiod_3.retired = 0 
                                AND policyperiod_3.temporarybranch = 0 
                                GROUP BY policyperiod_3.ID) pc_policyPeriod_PolicyHolder ON pc_policyPeriod_PolicyHolder.policyperiod_3ID = policyperiod_0.ID

        LEFT JOIN         pc_policycontactrole policyHolder_1 ON policyHolder_1.ID = pc_policyPeriod_PolicyHolder.policyHolderID


        LEFT JOIN              (SELECT policyPeriod_5.ID AS BranchID,
                                MAX(pc_policycontactrole_0.ID) vehicleOwnerID                   
                                FROM pcx_vehiclesubjectrole_ait    AS vehiclesubjectrole_ait_1              
                                INNER JOIN pcx_rolesforpolicysubject_ait AS rolesforpolicysubject_ait_2 ON  vehiclesubjectrole_ait_1.ID=rolesforpolicysubject_ait_2.VehicleSubjectRole                      
                                INNER JOIN pc_policyperiod  AS policyPeriod_5 ON policyPeriod_5.ID = rolesforpolicysubject_ait_2.BranchID
                                INNER JOIN pcx_subjectroles_ait AS subjectroles_ait_3 ON subjectroles_ait_3.id=rolesforpolicysubject_ait_2.subjectrole                      
                                INNER JOIN pc_policycontactrole AS pc_policycontactrole_0 ON vehiclesubjectrole_ait_1.Subject = pc_policycontactrole_0.ID
                                WHERE policyPeriod_5.retired = 0 
                                AND   subjectroles_ait_3.subjectrole = (SELECT TOP 1 ID FROM pctl_mtsubjectroles_ait WHERE TYPECODE = 'MAIN_OWNER') 
                                AND   subjectroles_ait_3.retired = 0
                                AND   policyPeriod_5.temporarybranch = 0 
                                AND   policyPeriod_5.PolicyNumber IS NOT NULL
                                GROUP BY policyPeriod_5.ID) pc_policyPeriod_VehicleOwner ON pc_policyPeriod_VehicleOwner.BranchID = policyperiod_0.ID

        LEFT JOIN               pc_policycontactrole vehicleOwner_1 ON vehicleOwner_1.ID = pc_policyPeriod_VehicleOwner.vehicleOwnerID

        LEFT JOIN               (SELECT policyChangeReason.PolicyChange as JobID, min(reason.TYPECODE) as ReasonTypecode
                                 FROM   pcx_policychangereason_ait policyChangeReason
                                 JOIN   pctl_changereason_ait reason on policyChangeReason.Reason = reason.ID
                                 WHERE  policyChangeReason.retired = 0
                                 GROUP BY policyChangeReason.PolicyChange) PolicyChangeReason ON PolicyChangeReason.JobID = job_2.ID

        LEFT JOIN               pctl_policychangeoperation_ait Operation ON Operation.ID = job_2.Operation_AIT

        LEFT JOIN               (SELECT SITANotificationWithRank.JobNumber as JobNumber,
                                        MAX(SITANotificationWithRank.NotificationID) as NotificationMaxID,
                                        MIN(SITANotificationWithRank.NotificationID) as NotificationMinID
                                 FROM (  SELECT notify.JobNumber as JobNumber,
                                                notify.CreateTime as CreateTime,
                                                notify.ID as NotificationID,
                                                rank() over (partition by notify.JobNumber order by notify.ID) as NotificationRank,
                                                rank() over (partition by notify.JobNumber, notify.CreateTime order by notify.ID) as NotificationSameCommitRank
                                         FROM   pcx_dailysitanotifications notify
                                         WHERE  notify.retired = 0
                                           AND notify.JobNumber is not null
                                           AND notify.CreatedManually = 0) as SITANotificationWithRank
                                 where (SITANotificationWithRank.NotificationRank = 1 and SITANotificationWithRank.NotificationSameCommitRank = 1)
                                    or (SITANotificationWithRank.NotificationRank = 2 and SITANotificationWithRank.NotificationSameCommitRank = 2)
                                 GROUP BY SITANotificationWithRank.JobNumber) SITANotificationJob ON SITANotificationJob.JobNumber = job_2.JobNumber
        LEFT JOIN               pcx_dailysitanotifications SITANotification ON SITANotificationJob.JobNumber = SITANotification.JobNumber AND SITANotificationJob.NotificationMaxID = SITANotification.ID
        LEFT JOIN               pctl_GenericRegistryStauts SITANotificationStatus ON SITANotification.Status = SITANotificationStatus.ID
        LEFT JOIN               pcx_dailysitanotifications SITANotificationPrevious ON SITANotificationJob.JobNumber = SITANotificationPrevious.JobNumber AND SITANotificationJob.NotificationMinID = SITANotificationPrevious.ID AND SITANotificationJob.NotificationMinID != SITANotificationJob.NotificationMaxID
        LEFT JOIN               pctl_GenericRegistryStauts SITANotificationPreviousStatus ON SITANotificationPrevious.Status = SITANotificationPreviousStatus.ID

        WHERE                   policyline_0.subtype = 2
        AND                     policyline_0.ExpirationDate IS NULL 
        AND                     groot.expirationdate IS NULL
        AND                     policyperiod_0.retired = 0 
        AND                     policyperiod_0.temporarybranch = 0
        AND                     policyperiod_0.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
        AND                     (job_2.SuspensionType_AIT is null or  job_2.SuspensionType_AIT !=  (SELECT id from pctl_suspensiontype_ait where typecode = 'morosita')) 
        AND                     policyperiod_0.policynumber IS NOT NULL
        AND                     (   policyperiod_0.id IN (SELECT     groot1.id col0
                                                          FROM       pc_policyperiod gRoot1
                                                          INNER JOIN pc_job AS job_2 ON job_2.id=groot1.jobid
                                                          WHERE      groot1.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                                          AND        groot1.policynumber IS NOT NULL
                                                          AND        groot1.retired = 0
                                                          AND        groot1.temporarybranch = 0
                                                          AND        CONVERT(date, job_2.closedate) = DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                                          AND        job_2.retired = 0))

    UNION

        SELECT          policyperiod_0.PolicyID                                                             ID_Policy_PC,
                        policyperiod_0.ID                                                                   ID_PolicyPeriod_PC,
                        job_2.JobNumber                                                                     JobNumber,
                        Installment.ReceivedDate                                                            Data_Chiusura_Transazione,
                        null                                                                                PolicyChangeReasonCode,
                        policyperiod_0.policynumber                                                         Numero_Polizza, 
                        gRoot.RegistrationNumber                                                            RegistrationNumber,
                        null                                                                                TipoMovimento,
                        null                                                                                CausaleMovimento,
                        null                                                                                TipoMovimentoPrecedente,
                        null                                                                                CausaleMovimentoPrecedente,
                        0                                                                                   NumeroTrigger,
                        SITANotification.ID                                                                 NotificationID_Triggerato,
                        SITANotification.TransmissionChannel                                                NotificationChannel_Triggerato,
                        SITANotification.MovementType                                                       TipoMovimento_Triggerato,
                        SITANotification.CauseCode                                                          CausaleMovimento_Triggerato,
                        SITANotificationStatus.TYPECODE                                                     NotificaStatus_Triggerato,
                        null                                                                                NotificationPrecedenteID_Triggerato,
                        null                                                                                NotificationPrecedenteChannel_Triggerato,
                        null                                                                                TipoMovimentoPrecedente_Triggerato,
                        null                                                                                CausaleMovimentoPrecedente_Triggerato,
                        null                                                                                NotificaStatusPrecedente_Triggerato,
                        1                                                                                   NumeroTrigger_Triggerato,
                        policyHolder_1.TaxIDInternal                                                        TaxIDInternalContraentePolizza,
                        policyHolder_1.CompanyNameInternal                                                  NomeCompagniaContraentePolizza,
                        policyHolder_1.FirstNameInternal                                                    NomeContraentePolizza,
                        policyHolder_1.LastNameInternal                                                     CognomeContraentePolizza,
                        vehicleOwner_1.TaxIDInternal                                                        TaxIDInternalProprietarioVeicolo,
                        vehicleOwner_1.CompanyNameInternal                                                  NomeCompagniaProprietarioVeicolo,
                        vehicleOwner_1.FirstNameInternal                                                    NomeContraenteProprietarioVeicolo, 
                        vehicleOwner_1.LastNameInternal                                                     CognomeContraenteProprietarioVeicolo,
                        iurcode_ait_11.code                                                                 Codice_IUR, 
                        CASE WHEN vehicleCoverage_Vehicle.Vehicle IS NOT NULL   THEN 1 ELSE 0 END           BlackBox,
                        case when (vehicleType.TYPECODE = 'car')        then 'A'
                             when (vehicleType.TYPECODE = 'motorcycle') then 'M'
                             when (vehicleType.TYPECODE = 'moped')      then 'W'
                             else null end                                                                  TipoVeicoloANIA,

                        0                                                                                   IsSubmission,
                        1                                                                                   IsNextInstallment,
                        0                                                                                   IsRenewal,
                        0                                                                                   IsPolicyChange,
                        0                                                                                   IsSuspension,
                        0                                                                                   SuspensionTypeToInclude,
                        0                                                                                   IsReactivation,
                        0                                                                                   IsCancellation,
                        0                                                                                   CancellationReasonCodeForA1,
                        0                                                                                   CancellationReasonCodeForI1,
                        0                                                                                   CancellationReasonCodeForI4,
                        0                                                                                   CancellationReasonCodeForI5,
                        0                                                                                   CancellationReasonCodeForI9,
                        0                                                                                   CancellationReasonCodeForI6,
                        0                                                                                   PolicyChangeReasonCodeToExclude,

                    convert(date, Installment.NextCoverageStartDate)                                    EditEffectiveDate,                  
                        '2359'                                                                              ChangeVehicleHour,

                        rank() over (partition by policyperiod_0.ID
                                     order by job_2.CloseDate desc,
                                              SITANotificationJob.CreateTime desc)                          idrank

        FROM            pcx_vehicle_ait gRoot 
        INNER JOIN      pc_policyperiod AS policyperiod_0 ON policyperiod_0.id=groot.branchid 
        INNER JOIN      pc_policy       AS policy_1 ON policy_1.id=policyperiod_0.policyid 
        LEFT  JOIN      pcx_iurcode_ait AS iurcode_ait_11 ON groot.id=iurcode_ait_11.vehicle
        INNER JOIN      pc_job AS job_2 ON job_2.id=policyperiod_0.jobid
        INNER JOIN      pc_policyline AS policyline_0 ON policyperiod_0.ID = policyline_0.BranchID 
        LEFT JOIN       (SELECT DISTINCT vehicleCoverage.Vehicle as Vehicle
                         FROM            pcx_vehiclecov_ait vehicleCoverage
                         WHERE           vehicleCoverage.ExpirationDate IS NULL
                         AND             vehicleCoverage.PatternCode = 'A009') vehicleCoverage_Vehicle ON gRoot.ID = vehicleCoverage_Vehicle.Vehicle
        INNER JOIN      pctl_mtvehicletype_ait as vehicleType ON vehicleType.ID = groot.vehicletype

        LEFT JOIN       (SELECT policyperiod_3.ID as policyperiod_3ID,
                                MAX(policyHolder_0.ID) policyHolderID
                                FROM pc_policycontactrole policyHolder_0 
                                INNER JOIN pc_policyperiod AS policyperiod_3 ON policyperiod_3.id=policyHolder_0.branchid 
                                WHERE policyHolder_0.subtype = (SELECT TOP 1 ID FROM pctl_policycontactrole WHERE TYPECODE = 'PolicyPriNamedInsured')
                                AND policyperiod_3.retired = 0 
                                AND policyperiod_3.temporarybranch = 0 
                                GROUP BY policyperiod_3.ID) pc_policyPeriod_PolicyHolder ON pc_policyPeriod_PolicyHolder.policyperiod_3ID = policyperiod_0.ID

        LEFT JOIN         pc_policycontactrole policyHolder_1 ON policyHolder_1.ID = pc_policyPeriod_PolicyHolder.policyHolderID

        LEFT JOIN              (SELECT policyPeriod_5.ID AS BranchID,
                                MAX(pc_policycontactrole_0.ID) vehicleOwnerID                   
                                FROM pcx_vehiclesubjectrole_ait    AS vehiclesubjectrole_ait_1              
                                INNER JOIN pcx_rolesforpolicysubject_ait AS rolesforpolicysubject_ait_2 ON  vehiclesubjectrole_ait_1.ID=rolesforpolicysubject_ait_2.VehicleSubjectRole                      
                                INNER JOIN pc_policyperiod  AS policyPeriod_5 ON policyPeriod_5.ID = rolesforpolicysubject_ait_2.BranchID
                                INNER JOIN pcx_subjectroles_ait AS subjectroles_ait_3 ON subjectroles_ait_3.id=rolesforpolicysubject_ait_2.subjectrole                      
                                INNER JOIN pc_policycontactrole AS pc_policycontactrole_0 ON vehiclesubjectrole_ait_1.Subject = pc_policycontactrole_0.ID
                                WHERE policyPeriod_5.retired = 0 
                                AND   subjectroles_ait_3.subjectrole = (SELECT TOP 1 ID FROM pctl_mtsubjectroles_ait WHERE TYPECODE = 'MAIN_OWNER') 
                                AND   subjectroles_ait_3.retired = 0
                                AND   policyPeriod_5.temporarybranch = 0 
                                AND   policyPeriod_5.PolicyNumber IS NOT NULL
                                GROUP BY policyPeriod_5.ID) pc_policyPeriod_VehicleOwner ON pc_policyPeriod_VehicleOwner.BranchID = policyperiod_0.ID

        LEFT JOIN               pc_policycontactrole vehicleOwner_1 ON vehicleOwner_1.ID = pc_policyPeriod_VehicleOwner.vehicleOwnerID

        INNER JOIN              (   select distinct PP_BC.PolicyNumber as PolicyNumber, 
                                                    PP_BC.TermNumber as TermNumber,
                                                    convert(date, BMR_BC.ReceivedDate) as ReceivedDate,
                                                    case when (BMR_BC.ReceivedDate > I_BC.PaymentDueDate)
                                                         then convert(date,BMR_BC.ReceivedDate)
                                                         else convert(date,I_BC.PaymentDueDate)
                                                    end as NextCoverageStartDate,
                                                    max(policyperiod_1.jobid) as installmentJob

                                    from {db_ref}.dbo.bc_PolicyPeriod PP_BC
                                    join {db_ref}.dbo.bc_InvoiceItem as II_BC on II_BC.PolicyPeriodID = PP_BC.ID
                                    join {db_ref}.dbo.bc_Invoice as I_BC on I_BC.ID = II_BC.InvoiceID
                                    join {db_ref}.dbo.bc_BaseDistItem as BDI_BC on BDI_BC.InvoiceItemID = II_BC.ID
                                    join {db_ref}.dbo.bc_BaseDist as BD_BC on BD_BC.ID = BDI_BC.ActiveDistID
                                    join {db_ref}.dbo.bc_BaseMoneyReceived BMR_BC on BMR_BC.BaseDistID = BD_BC.ID
                                    join pc_policyperiod policyperiod_1 on policyperiod_1.policyNumber = PP_BC.PolicyNumber 
                                                                            and policyperiod_1.termNumber =  PP_BC.termNumber 
                                                                            and policyperiod_1.retired = 0 
                                                                            and policyperiod_1.temporarybranch = 0  
                                                                            and policyperiod_1.Status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                    join pc_job job_5 on job_5.id = policyperiod_1.jobid
                                    where PP_BC.Retired = 0
                                      and PP_BC.PolicyNumber is not null
                                      and PP_BC.TermNumber is not null
                                      and II_BC.Retired = 0
                                      and II_BC.Type in (select ID from {db_ref}.dbo.bctl_InvoiceItemType where TYPECODE = 'installment')
                                      and II_BC.PaidAmount > 0
                                      and I_BC.Retired = 0
                                      and BDI_BC.Retired = 0
                                      and BD_BC.Retired = 0
                                      and BMR_BC.Retired = 0
                                      and BMR_BC.Subtype in (select ID from {db_ref}.dbo.bctl_BaseMoneyReceived where TYPECODE in ('AgencyBillMoneyRcvd','DirectBillMoneyRcvd','PaymentMoneyReceived','ZeroDollarAMR','ZeroDollarDMR','ZeroDollarReversal','BaseMoneyReceived'))
                                      and convert(date, BMR_BC.ReceivedDate) = DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                      and convert(date,job_5.createtime) <= DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))

                                      GROUP BY PP_BC.PolicyNumber, PP_BC.TermNumber, BMR_BC.ReceivedDate, I_BC.PaymentDueDate
                             ) Installment on Installment.PolicyNumber = policyperiod_0.PolicyNumber 
                                              and Installment.TermNumber = policyperiod_0.TermNumber
                                              and Installment.installmentJob = job_2.id

        LEFT JOIN           (   SELECT notify.JobNumber as JobNumber,
                                       notify.ID as NotificationID,
                                       notify.CreateTime as CreateTime,
                                       notify.MovementType as MovementType,
                                       notify.CauseCode as CauseCode
                                FROM pcx_dailysitanotifications notify
                                WHERE notify.retired = 0
                                  AND notify.CreateUserID = (select U.ID from pc_user as U join pc_credential CR on U.CredentialID = CR.ID where CR.UserName = 'fwbatch.systemuser')
                                  AND notify.JobNumber is not null
                                  AND notify.CreatedManually = 0) SITANotificationJob ON SITANotificationJob.JobNumber = job_2.JobNumber
                                                                                        and SITANotificationJob.CreateTime > Installment.ReceivedDate
                                                                                        and SITANotificationJob.MovementType = 'C'
                                                                                        and SITANotificationJob.CauseCode = '0'
        LEFT JOIN               pcx_dailysitanotifications SITANotification ON SITANotificationJob.JobNumber = SITANotification.JobNumber AND SITANotificationJob.NotificationID = SITANotification.ID
        LEFT JOIN               pctl_GenericRegistryStauts SITANotificationStatus ON SITANotification.Status = SITANotificationStatus.ID

        WHERE                   policyline_0.subtype = 2
        AND                     policyline_0.ExpirationDate IS NULL 
        AND                     groot.expirationdate IS NULL
        AND                     policyperiod_0.retired = 0 
        AND                     policyperiod_0.temporarybranch = 0
        AND                     policyperiod_0.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
        AND                     policyperiod_0.policynumber IS NOT NULL

    ) Base 
    LEFT JOIN               (
                            SELECT          policyperiod_0.PolicyID                                                             ID_Policy_PC,
                                            policyperiod_0.ID                                                                   ID_PolicyPeriod_PC,
                                            job_2.JobNumber                                                                     JobNumber,
                                            job_2.CloseDate                                                                     Data_Chiusura_Transazione,
                                            policyperiod_0.policynumber                                                         Numero_Polizza, 
                                            gRoot.RegistrationNumber                                                            RegistrationNumber,
                                            policyHolder_1.TaxIDInternal                                                        TaxIDInternalContraentePolizza,
                                            policyHolder_1.CompanyNameInternal                                                  NomeCompagniaContraentePolizza,
                                            policyHolder_1.FirstNameInternal                                                    NomeContraentePolizza,
                                            policyHolder_1.LastNameInternal                                                     CognomeContraentePolizza,
                                            vehicleOwner_1.TaxIDInternal                                                        TaxIDInternalProprietarioVeicolo,
                                            vehicleOwner_1.CompanyNameInternal                                                  NomeCompagniaProprietarioVeicolo,
                                            vehicleOwner_1.FirstNameInternal                                                    NomeContraenteProprietarioVeicolo, 
                                            vehicleOwner_1.LastNameInternal                                                     CognomeContraenteProprietarioVeicolo,
                                            iurcode_ait_11.code                                                                 Codice_IUR, 
                                            CASE WHEN vehicleCoverage_Vehicle.Vehicle IS NOT NULL   THEN 1 ELSE 0 END           BlackBox,
                                            case when (vehicleType.TYPECODE = 'car')        then 'A'
                                                 when (vehicleType.TYPECODE = 'motorcycle') then 'M'
                                                 when (vehicleType.TYPECODE = 'moped')      then 'W'
                                                 else null end                                                                  TipoVeicoloANIA,

                                            convert(date, policyperiod_0.EditEffectiveDate)                                     EditEffectiveDate,                  
                                            REPLACE(CONVERT(varchar(5), gRoot.ChangeVehicleHour, 108), ':', '')                 ChangeVehicleHour

                            FROM            pcx_vehicle_ait gRoot 
                            INNER JOIN      pc_policyperiod AS policyperiod_0 ON policyperiod_0.id=groot.branchid 
                            INNER JOIN      pc_policy       AS policy_1 ON policy_1.id=policyperiod_0.policyid 
                            LEFT  JOIN      pcx_iurcode_ait AS iurcode_ait_11 ON groot.id=iurcode_ait_11.vehicle
                            INNER JOIN      pc_job AS job_2 ON job_2.id=policyperiod_0.jobid
                            INNER JOIN      pc_policyline AS policyline_0 ON policyperiod_0.ID = policyline_0.BranchID 
                            LEFT JOIN       (SELECT DISTINCT vehicleCoverage.Vehicle as Vehicle
                                             FROM            pcx_vehiclecov_ait vehicleCoverage
                                             WHERE           vehicleCoverage.ExpirationDate IS NULL
                                             AND             vehicleCoverage.PatternCode = 'A009') vehicleCoverage_Vehicle ON gRoot.ID = vehicleCoverage_Vehicle.Vehicle
                            INNER JOIN      pctl_mtvehicletype_ait as vehicleType ON vehicleType.ID = groot.vehicletype

                            LEFT JOIN       (SELECT policyperiod_3.ID as policyperiod_3ID,
                                                    MAX(policyHolder_0.ID) policyHolderID
                                                    FROM pc_policycontactrole policyHolder_0 
                                                    INNER JOIN pc_policyperiod AS policyperiod_3 ON policyperiod_3.id=policyHolder_0.branchid 
                                                    WHERE policyHolder_0.subtype = (SELECT TOP 1 ID FROM pctl_policycontactrole WHERE TYPECODE = 'PolicyPriNamedInsured')
                                                    AND policyperiod_3.retired = 0 
                                                    AND policyperiod_3.temporarybranch = 0 
                                                    GROUP BY policyperiod_3.ID) pc_policyPeriod_PolicyHolder ON pc_policyPeriod_PolicyHolder.policyperiod_3ID = policyperiod_0.ID

                            LEFT JOIN         pc_policycontactrole policyHolder_1 ON policyHolder_1.ID = pc_policyPeriod_PolicyHolder.policyHolderID

                            LEFT JOIN              (SELECT policyPeriod_5.ID AS BranchID,
                                                    MAX(pc_policycontactrole_0.ID) vehicleOwnerID                   
                                                    FROM pcx_vehiclesubjectrole_ait    AS vehiclesubjectrole_ait_1              
                                                    INNER JOIN pcx_rolesforpolicysubject_ait AS rolesforpolicysubject_ait_2 ON  vehiclesubjectrole_ait_1.ID=rolesforpolicysubject_ait_2.VehicleSubjectRole                      
                                                    INNER JOIN pc_policyperiod  AS policyPeriod_5 ON policyPeriod_5.ID = rolesforpolicysubject_ait_2.BranchID
                                                    INNER JOIN pcx_subjectroles_ait AS subjectroles_ait_3 ON subjectroles_ait_3.id=rolesforpolicysubject_ait_2.subjectrole                      
                                                    INNER JOIN pc_policycontactrole AS pc_policycontactrole_0 ON vehiclesubjectrole_ait_1.Subject = pc_policycontactrole_0.ID
                                                    WHERE policyPeriod_5.retired = 0 
                                                    AND   subjectroles_ait_3.subjectrole = (SELECT TOP 1 ID FROM pctl_mtsubjectroles_ait WHERE TYPECODE = 'MAIN_OWNER') 
                                                    AND   subjectroles_ait_3.retired = 0
                                                    AND   policyPeriod_5.temporarybranch = 0 
                                                    AND   policyPeriod_5.PolicyNumber IS NOT NULL
                                                    GROUP BY policyPeriod_5.ID) pc_policyPeriod_VehicleOwner ON pc_policyPeriod_VehicleOwner.BranchID = policyperiod_0.ID

                            LEFT JOIN               pc_policycontactrole vehicleOwner_1 ON vehicleOwner_1.ID = pc_policyPeriod_VehicleOwner.vehicleOwnerID

                            WHERE                   policyline_0.subtype = 2
                            AND                     policyline_0.ExpirationDate IS NULL 
                            AND                     groot.expirationdate IS NULL
                            AND                     policyperiod_0.retired = 0 
                            AND                     policyperiod_0.temporarybranch = 0
                            AND                     policyperiod_0.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                            AND                     policyperiod_0.policynumber IS NOT NULL

                            AND                     (   policyperiod_0.id IN (SELECT     groot1.id col0
                                                          FROM       pc_policyperiod gRoot1
                                                          INNER JOIN pc_job AS job_2 ON job_2.id=groot1.jobid
                                                          WHERE      groot1.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                                          AND        groot1.policynumber IS NOT NULL
                                                          AND        groot1.retired = 0
                                                          AND        groot1.temporarybranch = 0
                                                          AND        CONVERT(date, job_2.closedate, 103) = DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                                          AND        job_2.retired = 0)
                                                    OR policyperiod_0.id IN (SELECT     Max(gRoot2.id) col0
                                                                              FROM       pc_policyperiod gRoot2
                                                                              INNER JOIN pc_job AS job_3 ON job_3.id=gRoot2.jobid
                                                                              WHERE      gRoot2.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                                                              AND        gRoot2.policynumber IS NOT NULL
                                                                              AND        gRoot2.retired = 0
                                                                              AND        gRoot2.temporarybranch = 0
                                                                              AND        CONVERT(date, job_3.closedate, 103) < DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                                                              AND        job_3.retired = 0
                                                                                     AND gRoot2.policyid IN (SELECT     gRoot3.policyid col0
                                                                                                             FROM       pc_policyperiod gRoot3
                                                                                                             INNER JOIN pc_job AS job_4 ON job_4.id=gRoot3.jobid
                                                                                                             WHERE      gRoot3.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                                                                                             AND        gRoot3.policynumber IS NOT NULL
                                                                                                             AND        gRoot3.retired = 0
                                                                                                             AND        gRoot3.temporarybranch = 0
                                                                                                             AND        CONVERT(date, job_4.closedate, 103) = DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                                                                                             AND        job_4.retired = 0)      
                                                                              GROUP BY   gRoot2.policyid
                                                                              HAVING     gRoot2.policyid IS NOT NULL))) Previous ON Previous.ID_Policy_PC = Base.ID_Policy_PC AND Previous.Data_Chiusura_Transazione < Base.Data_Chiusura_Transazione
        LEFT JOIN (
            SELECT          policyperiod_0.PolicyID                             ID_Policy_PC,
                            policyperiod_0.ID                                   ID_PolicyPeriod_PC,
                            job_2.JobNumber                                     JobNumber,
                            job_2.CloseDate                                     Data_Chiusura_Transazione,
                            policyperiod_0.policynumber                         Numero_Polizza, 
                            case when (suspensionType.TYPECODE in (
                                    'volontaria',
                                    'richiesta_compagnia')) then 1 else 0 end   SuspensionTypeToInclude

            FROM            pc_policyperiod AS policyperiod_0
            INNER JOIN      pc_policy       AS policy_1 ON policy_1.id=policyperiod_0.policyid 
            INNER JOIN      pc_job AS job_2 ON job_2.id=policyperiod_0.jobid
            INNER JOIN      pctl_suspensiontype_ait suspensionType ON suspensionType.ID = job_2.SuspensionType_AIT
            INNER JOIN      pctl_job as jobSubtype ON jobSubtype.ID = job_2.subtype
            INNER JOIN      pctl_policychangeoperation_ait Operation ON Operation.ID = job_2.Operation_AIT

            WHERE           policyperiod_0.retired = 0 
            AND             policyperiod_0.temporarybranch = 0
            AND             policyperiod_0.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
            AND             policyperiod_0.policynumber IS NOT NULL
            AND             jobSubtype.TYPECODE = 'PolicyChange'
            AND             Operation.TYPECODE = 'suspensionPolicy'
            AND             (policyperiod_0.PolicyID IN (   SELECT     groot1.PolicyID col0
                                                            FROM       pc_policyperiod gRoot1
                                                            INNER JOIN pc_job AS job_2 ON job_2.id=groot1.jobid
                                                            WHERE      groot1.status = (SELECT ID FROM pctl_policyperiodstatus WHERE TYPECODE = 'Bound')
                                                            AND        groot1.policynumber IS NOT NULL
                                                            AND        groot1.retired = 0
                                                            AND        groot1.temporarybranch = 0
                                                            AND        CONVERT(date, job_2.closedate, 103) = DATEFROMPARTS(YEAR('{selectedDate}'), MONTH('{selectedDate}'), DAY('{selectedDate}'))
                                                            AND        job_2.retired = 0))) Suspensions ON Suspensions.ID_Policy_PC = Base.ID_Policy_PC AND Suspensions.Data_Chiusura_Transazione < Base.Data_Chiusura_Transazione
                                                            WHERE Base.idrank = 1) as Final
 WHERE Final.idrank = 1
	 and ((Final.base_tipomovimento is not null and final.base_notificationid_triggerato is null) or (Final.base_tipomovimentoprecedente is not null and final.base_notificationprecedenteid_triggerato is null))
 )as temp2
"""

print(querona)