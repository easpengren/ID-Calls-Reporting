CD_CONTACT_TYPE_QUERY = """
SELECT cd,
  sum(case when status_name ='Busy Auto' or status_name = 'Busy' or status_name = 'Disconnected Number' or status_name = 'Outbound Pre-routing Drop' or status_name = 'Busy Auto' or status_name = 'Lead Being Called' or status_name = 'No Answer Autodial' or status_name = 'Hung up' or status_name = 'Outbound Local Channel Res Err' or status_name = 'Answering Machine' or status_name = 'Lead To Be Called' or status_name = 'Wrong Number' or status_name = 'Disconnected Number Auto' or status_name = 'Answering Machine Auto' or status_name = 'Agent Not Available' or status_name is null or status_name = 'DO NOT CALL'
      then 1 end) as no_contact,
  sum(case when status_name = 'No-Not voting' then 1 end) as not_voting,
  sum(case when status_name = 'Wont Tell' then 1 end) as wont_tell,
  sum(case when status_name = 'VoteEarly' then 1 end) as vote_early,
  sum(case when status_name = 'Call Back' then 1 end) as call_back,
  sum(case when status_name = 'VoteByMail' then 1 end) as vote_by_mail,
  sum(case when status_name = 'Yes - Will Support' then 1 end) as yes_will_support,
  sum(case when status_name = 'VoteInPerson' then 1 end) as vote_in_person,
  sum(case when status_name = 'Undecided' then 1 end) as undecided,
  sum(case when status_name = 'Not Interested' then 1 end) as not_interested
  
FROM collectivepac.id_calls_match
where status_name is not null
GROUP BY cd
order by cd;
"""
SD_CONTACT_TYPE_QUERY = """
SELECT sd,
  sum(case when status_name ='Busy Auto' or status_name = 'Busy' or status_name = 'Disconnected Number' or status_name = 'Outbound Pre-routing Drop' or status_name = 'Busy Auto' or status_name = 'Lead Being Called' or status_name = 'No Answer Autodial' or status_name = 'Hung up' or status_name = 'Outbound Local Channel Res Err' or status_name = 'Answering Machine' or status_name = 'Lead To Be Called' or status_name = 'Wrong Number' or status_name = 'Disconnected Number Auto' or status_name = 'Answering Machine Auto' or status_name = 'Agent Not Available' or status_name is null or status_name = 'DO NOT CALL'
      then 1 end) as no_contact,
  sum(case when status_name = 'No-Not voting' then 1 end) as not_voting,
  sum(case when status_name = 'Wont Tell' then 1 end) as wont_tell,
  sum(case when status_name = 'VoteEarly' then 1 end) as vote_early,
  sum(case when status_name = 'Call Back' then 1 end) as call_back,
  sum(case when status_name = 'VoteByMail' then 1 end) as vote_by_mail,
  sum(case when status_name = 'Yes - Will Support' then 1 end) as yes_will_support,
  sum(case when status_name = 'VoteInPerson' then 1 end) as vote_in_person,
  sum(case when status_name = 'Undecided' then 1 end) as undecided,
  sum(case when status_name = 'Not Interested' then 1 end) as not_interested

FROM collectivepac.id_calls_match
where status_name is not null
GROUP BY sd
order by sd;
"""
HD_CONTACT_TYPE_QUERY = """
SELECT hd,
  sum(case when status_name ='Busy Auto' or status_name = 'Busy' or status_name = 'Disconnected Number' or status_name = 'Outbound Pre-routing Drop' or status_name = 'Busy Auto' or status_name = 'Lead Being Called' or status_name = 'No Answer Autodial' or status_name = 'Hung up' or status_name = 'Outbound Local Channel Res Err' or status_name = 'Answering Machine' or status_name = 'Lead To Be Called' or status_name = 'Wrong Number' or status_name = 'Disconnected Number Auto' or status_name = 'Answering Machine Auto' or status_name = 'Agent Not Available' or status_name is null or status_name = 'DO NOT CALL'
      then 1 end) as no_contact,
  sum(case when status_name = 'No-Not voting' then 1 end) as not_voting,
  sum(case when status_name = 'Wont Tell' then 1 end) as wont_tell,
  sum(case when status_name = 'VoteEarly' then 1 end) as vote_early,
  sum(case when status_name = 'Call Back' then 1 end) as call_back,
  sum(case when status_name = 'VoteByMail' then 1 end) as vote_by_mail,
  sum(case when status_name = 'Yes - Will Support' then 1 end) as yes_will_support,
  sum(case when status_name = 'VoteInPerson' then 1 end) as vote_in_person,
  sum(case when status_name = 'Undecided' then 1 end) as undecided,
  sum(case when status_name = 'Not Interested' then 1 end) as not_interested

FROM collectivepac.id_calls_match
where status_name is not null
GROUP BY hd
order by hd;
"""

CD_PENETRATION_QUERY = """
create temp table cd_calls  as select cd,
  sum(case when status_name is not null then 1 else 0 end) as attempted,
  sum(case when status_name is not null then 0 else 1 end) as not_attempted  
FROM collectivepac.id_calls_match
GROUP BY cd
order by cd;


alter table cd_calls add column total decimal;
alter table cd_calls add column percent_dialed decimal;

update cd_calls set total = (attempted+not_attempted); 
update cd_calls set percent_dialed = (attempted/total)*100;

select * from cd_calls
order by cd;
"""

SD_PENETRATION_QUERY = """
create temp table sd_calls  as select sd,
  sum(case when status_name is not null then 1 else 0 end) as attempted,
  sum(case when status_name is not null then 0 else 1 end) as not_attempted  
FROM collectivepac.id_calls_match
GROUP BY sd
order by sd;


alter table sd_calls add column total decimal;
alter table sd_calls add column percent_dialed decimal;

update sd_calls set total = (attempted+not_attempted); 
update sd_calls set percent_dialed = (attempted/total)*100;

select * from sd_calls
order by sd;
"""

HD_PENETRATION_QUERY = """
create temp table hd_calls  as select hd,
  sum(case when status_name is not null then 1 else 0 end) as attempted,
  sum(case when status_name is not null then 0 else 1 end) as not_attempted  
FROM collectivepac.id_calls_match
GROUP BY hd
order by hd;


alter table hd_calls add column total decimal;
alter table hd_calls add column percent_dialed decimal;

update hd_calls set total = (attempted+not_attempted); 
update hd_calls set percent_dialed = (attempted/total)*100;

select * from hd_calls
order by hd;
"""