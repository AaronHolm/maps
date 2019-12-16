import pandas as pd

def sa_goals_file(output_loc, goals_loc):
  df = pd.read_csv(output_loc)
  df = df[['state', 'sa_active', 'sa_active_num', 'sa_rep', 'sa_rep_title', 'sa_rep_region', 'sa_rep_img', 'mem_rep', 'mem_rep_title', 'mem_rep_region', 'mem_rep_img', 'resi_mw', 'nonresi_mw', 'utility_mw']]
  goals_df = xlgoals_to_html(goals_loc)
  df = df.merge(goals_df, how='left', on='state')

  # Fill in blanks
  blank_state = "While not an active state for the State Affairs team, we're always monitoring for significant activity and work with partners where available should the need arise."
  df.loc[:, 'state_goals'] = [set_goal(blank_state) if pd.isnull(x) else x for x in df['state_goals']]

  df.to_csv(output_loc, index=False)
  return

def xlgoals_to_html(loc):
  df = pd.read_excel(loc, skiprows=1)
  df.rename(columns={'Q4 Progress': 'progress'}, inplace=True)
  output_html = []
  for state in df['state'].unique():
    tmp_df = df[df['state'] == state]
    row_html = ''
    for i, row in tmp_df.iterrows():
      goal_html = set_goal(row['goal'])
      progress_html = set_progress(str(row['progress']))
      #row_html = [row['state'], goal_html + progress_html]
      row_html += goal_html + progress_html
    output_html.append([state, row_html])
  output_df = pd.DataFrame(data=output_html, columns=['state', 'state_goals'])


  return output_df

def set_goal(goal_text):
  goal_html = '<p class="goal">' + goal_text + '</p>'
  return goal_html

def set_progress(progress_text):
  progress_html = '<p class="progress">' + progress_text + '</p>'
  return progress_html

if __name__ == '__main__':
  base = '/mnt/c/Users/AHolm/Work Folders/Documents/Maps/SA Goals Map/'
  #raw_goals = 'SEIA-State-Policy-Map-Data_Q22019 4-16-19.xlsx'
  raw_goals = 'SEIA-State-Policy-Map-Data_Q32019 8-1-19.xlsx'
  output_file = 'sa_goals.csv'
  sa_goals_file(base+output_file, base+raw_goals)
  #df = xlgoals_to_html(base+raw_goals)
  #df.to_excel(base + 'xlgoals_to_html.xlsx')
  #print(df.head())
