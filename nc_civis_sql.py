CD_CONTACT_TYPE_QUERY = """
SELECT vb_vf_cd,
  sum(case when status_name ='Busy Auto' or status_name = 'Busy' or status_name = 'Disconnected Number' or status_name = 'Outbound Pre-routing Drop' or status_name = 'Busy Auto' or status_name = 'Lead Being Called' or status_name = 'No Answer Autodial' or status_name = 'Hung up' or status_name = 'Outbound Local Channel Res Err' or status_name = 'Answering Machine' or status_name = 'Lead To Be Called' or status_name = 'Wrong Number' or status_name = 'Disconnected Number Auto' or status_name = 'Answering Machine Auto' or status_name = 'Agent Not Available' or status_name is null or status_name = 'DO NOT CALL'
      then 1 end) as no_contact,
  sum(case when status_name = 'No-Not voting' then 1 end) as not_voting,
  sum(case when status_name = 'Wont Tell' then 1 end) as wont_tell,
  sum(case when status_name = 'Call Back' then 1 end) as call_back,
  sum(case when status_name = 'Yes - Will Support' then 1 end) as contacted,
  sum(case when status_name = 'Undecided' then 1 end) as undecided,
  sum(case when status_name = 'Not Interested' then 1 end) as not_interested

FROM collectivepac.nc_calls_vanid
where status_name is not null
and state='NC'
GROUP BY vb_vf_cd
order by vb_vf_cd;
"""
