import os
from tqdm import tqdm
import re


def load_solutions(samples_dir, ext):
    files = os.listdir(samples_dir)
    solution_paths = []
    for file in files:
        if file.endswith(ext):
            solution_paths.append(os.path.join(samples_dir, file))

    return solution_paths


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--eofs", nargs="+", type=str, default=[])
    parser.add_argument("--remove_prompt", action="store_true")
    parser.add_argument("--source_lang", required=True, type=str, choices=["Java", "Python"])
    parser.add_argument("--target_lang", required=True, type=str, choices=["Java", "Python"])
    parser.add_argument("--rm-prefix-lines", nargs="+", type=str, help="Remove lines starting with these string.", default=[])
    parser.add_argument("--der", action='store_true')
    parser.add_argument('--use_test', help='use test dataset', action='store_true')
    parser.add_argument('--use_misleading_test', help='use test dataset', action='store_true')
    parser.add_argument('--no_test', help='use test dataset', action='store_true')
    args = parser.parse_args()

    EXTENSIONS = { "Java": ".java", "Python": ".py" }
    if args.der:
        task='DER'
    else:
        task='SR'
    if args.use_test:
        folder_path=f"../Experiment_Results/intermediate/{task}/Translation/use_test/{args.model.split('/')[-1]}/{args.dataset}/{args.source_lang}/{args.target_lang}"
    elif args.use_misleading_test:
        folder_path=f"../Experiment_Results/intermediate/{task}/Translation/misleading/{args.model.split('/')[-1]}/{args.dataset}/{args.source_lang}/{args.target_lang}"
    else:
        folder_path=f"../Experiment_Results/intermediate/{task}/Translation/no_test/{args.model.split('/')[-1]}/{args.dataset}/{args.source_lang}/{args.target_lang}"
    # make a new folder with "-sanitized" suffix
    target_path = folder_path + "-sanitized"
    target_path = str(target_path)
    os.makedirs(target_path, exist_ok=True)

    for solution_path in tqdm(load_solutions(folder_path, EXTENSIONS[args.target_lang])):

        filename = os.path.basename(solution_path)

        with open(solution_path, "r") as f:
            solution = f.read()
        old_code = solution

        # start to modify old_code | old_code should not be re-defined

        new_code = old_code
        # print(args.remove_prompt, solution_path)
        # exit(0)
        if args.remove_prompt and ('CodeLlama' in solution_path or 'mistral' in solution_path):
            # new_code = new_code[new_code.find("[/INST]") + len("[/INST]"):]
            new_code = new_code.split("[/INST]")[-1]
        
        if args.remove_prompt and 'Magicoder' in solution_path:
            # new_code = new_code[new_code.find("@@ Response") + len("@@ Response"):]
            new_code = new_code.split("@@ Response")[-1]
        
        if args.remove_prompt and ('deepseek-coder' in solution_path or 'wizardcoder' in solution_path):
            # new_code = new_code[new_code.find("### Response:") + len("### Response:"):
            new_code = new_code.split("### Response:")[-1]

        if args.remove_prompt and 'starcoder' in solution_path and 'starcoder2' not in solution_path:
            new_code = new_code[new_code.find("<fim_suffix><fim_middle>") + len("<fim_suffix><fim_middle>"):]
            new_code = new_code.split("<fim_suffix><fim_middle>")[-1]
        
        if args.remove_prompt and 'llama2' in solution_path:
            new_code = new_code[new_code.find("###") + len("###"):]
        
        if 'granite' in solution_path:
            try:
                new_code = new_code.split("Answer:")[1].split(f"```{args.target_lang.lower()}")[1].split("```")[0]
            except:
                new_code = ""

        if 'gpt' in solution_path or 'gpt-3.5' in solution_path or 'codeqwen' in solution_path:
            new_code = new_code
            # new_code = new_code[new_code.find(f"```{args.target_lang.lower()}") + len(f"```{args.target_lang.lower()}"):
            #                     new_code.find("```", new_code.find(f"```{args.target_lang.lower()}") + len(f"```{args.target_lang.lower()}"))]
        
        if "```java" in new_code:
            new_code = (new_code.split("```java")[-1]).split("```")[0]
        else:
            if len(new_code.split("```")) >2:
                new_code = new_code.split("```")[-2]
            elif len(new_code.split("```")) ==2:
                new_code = new_code.split("```")[-1]
        # exit(0)
        # new_code0 = new_code[new_code.find(f"```{args.target_lang.lower()}") + len(f"```{args.target_lang.lower()}"):]
        # new_code = new_code0[:new_code0.find("```", new_code0.find(f"```{args.target_lang.lower()}") + len(f"```{args.target_lang.lower()}"))]
        
        # basic handling of chat output
        new_code = new_code.replace(f"```{args.target_lang.lower()}", "").replace("```", "").strip()

        for prefix in args.rm_prefix_lines:
            new_code = "\n".join(
                [
                    line
                    for line in new_code.splitlines()
                    if not line.startswith(prefix)
                ]
            ).strip()

        for eof in args.eofs:
            new_code = new_code.split(eof)[0].strip()


        if args.target_lang == "java" or "Java":
            new_code = re.sub('public\s*class\s*.+', 'public class ' + filename.split('.')[0] + ' {', new_code)
        with open(target_path + "/" + filename, "w") as f:
            f.write(new_code)
