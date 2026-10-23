"""Execute this trusted local notebook in order and retain bounded text outputs.

Uses standard-library AST execution instead of requiring a Jupyter server.
Run only reviewed notebooks: code cells execute with normal Python permissions.
"""
import ast
from contextlib import redirect_stdout
import io
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
path=ROOT/'IFT103_SQL_Resource_Analytics.ipynb'
book=json.loads(path.read_text())
assert book['nbformat']==4 and isinstance(book['cells'],list)
scope={'__name__':'__main__'}
for count,cell in enumerate((c for c in book['cells'] if c['cell_type']=='code'),1):
    source=''.join(cell['source'])
    tree=ast.parse(source)
    output=io.StringIO()
    with redirect_stdout(output):
        if tree.body and isinstance(tree.body[-1],ast.Expr):
            last=tree.body.pop()
            exec(compile(tree,str(path),'exec'),scope)
            value=eval(compile(ast.Expression(last.value),str(path),'eval'),scope)
            if value is not None:
                print(value.to_string(max_rows=10) if hasattr(value,'to_string') else repr(value))
        else:
            exec(compile(tree,str(path),'exec'),scope)
    cell['execution_count']=count
    cell['outputs']=[{'output_type':'stream','name':'stdout','text':output.getvalue().splitlines(keepends=True)}] if output.getvalue() else []
assert len(scope['df'])==scope['conn'].execute('SELECT COUNT(*) FROM process_metrics').fetchone()[0]
assert len(scope['df_high_cpu'])==len(scope['pd'].read_excel(scope['export_path']))
assert scope['df_high_cpu']['CPU %'].gt(30).all()
scope['conn'].close()
path.write_text(json.dumps(book,indent=1)+'\n')
print(f'Executed all code cells: {len(scope["df"])} input rows; {len(scope["df_high_cpu"])} exported rows. Counts and threshold verified.')
