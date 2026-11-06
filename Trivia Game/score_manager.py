def calculate_percentage(correct_answers, total_questions):
    return (correct_answers / total_questions) * 100

def build_result(correct_answers, total_questions, percentage, time_taken, user_config):
    hours, minutes, seconds = time_taken
    if hours == 1:
        hours = f"{int(hours)} hour"
    else:
        hours = f"{int(hours)} hours"

    if minutes == 1:
        minutes = f"{int(minutes)} minute"
    else:
        minutes = f"{int(minutes)} minutes"

    if seconds == 1:
        seconds = f"{int(seconds)} second"
    else:
        seconds = f"{seconds} seconds"

    wrong_answers = total_questions - correct_answers
    player_data = {
        "correct_answers": correct_answers,
        "wrong_answers": wrong_answers,
        "total_questions": total_questions,
        "percentage": percentage,
        "time_taken": f"{hours} {minutes} {seconds}"
    }
    player_data.update(user_config)
    return player_data