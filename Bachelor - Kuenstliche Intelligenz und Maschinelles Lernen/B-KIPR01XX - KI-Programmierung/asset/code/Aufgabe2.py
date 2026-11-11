FUEL_MAP = {0: 0, 1: 1, 2: 5, 3: 1} # noop, left, main, right
df_steps["fuel_step"] = df_steps["action"].map(FUEL_MAP)
df_episodes["fuel_episode"] = (df_steps.groupby("episode_id")["fuel_step"].sum())